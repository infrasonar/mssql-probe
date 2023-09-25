import asyncio
import datetime
import decimal
import pytds
import logging
import uuid
from libprobe.asset import Asset
from libprobe.exceptions import CheckException
from pytds.login import NtlmAuth
from typing import List, Optional
from .asset_cache import AssetCache

APPNAME = 'Infrasonar mssql-probe'
DEFAULT_MSSQL_PORT = 1433


def _get_conn(host, port, username, password, dbname=None):
    auth = NtlmAuth(username, password) if '\\' in username else None
    return pytds.connect(
        host,
        dbname,
        username,
        password,
        port=port,
        auth=auth,
        appname=APPNAME
    )


def _get_data(host, port, username, password, qry, db, *_):
    with _get_conn(host, port, username, password, db) as conn:
        with conn.cursor() as cur:
            cur.execute(qry)
            res = cur.fetchall()
            collnames = [tup[0] for tup in cur.description]
            return collnames, res


def _get_data_each_db(host, port, username, password, qry, _db, min_level):
    with _get_conn(host, port, username, password) as conn:
        dbs, expired = AssetCache.get_value((host, port, 'dbnames'))
        if dbs is None or expired:
            dbs = _get_db_names(conn)
            AssetCache.set_value((host, port, 'dbnames'), dbs, 900)

        # blame [msdb] for our CPU usage. Since we otherwise are blaming
        # the measured instances
        with conn.cursor() as cur:
            cur.execute('USE [msdb];\r\n{}'.format(qry))
            cur.fetchall()

        res = []
        collnames = []
        for db, compatibility_level in dbs:
            if min_level is not None and compatibility_level < min_level:
                continue
            try:
                with conn.cursor() as cur:
                    cur.execute('USE [{}];\r\n{}'.format(db, qry))
                    if not collnames:
                        collnames = [tup[0] for tup in cur.description]
                    res.extend(cur.fetchall())
            except Exception as ex:
                msg = str(ex)
                if 'cannot be opened. It is in the middle of a restore' in msg:
                    continue
                else:
                    raise
        return collnames, res


def _get_db_names(conn):
    with conn.cursor() as cur:
        cur.execute('''
            SELECT name, compatibility_level FROM sys.databases
            WHERE name not in ('master', 'tempdb', 'model', 'msdb')
        ''')
        res = cur.fetchall()
        return res


async def get_data(
        asset: Asset,
        asset_config: dict,
        config: dict,
        query: str,
        idx: Optional[List[str]] = ['name'],
        db: Optional[str] = None,
        each_db: Optional[bool] = False,
        min_compatibility_level: Optional[int] = None) -> list:
    address = config.get('address')
    if not address:
        address = asset.name
    assert asset_config, 'missing credentials'
    instance = config.get('instance', '')
    if instance:
        address = f'{address}\\{instance}'
        port = None
    else:
        port = config.get('port', DEFAULT_MSSQL_PORT)

    try:
        func = _get_data_each_db if each_db \
            else _get_data
        colnames, rows = await asyncio.get_event_loop().run_in_executor(
            None,
            func,
            address,
            port,
            asset_config['username'],
            asset_config['password'],
            query,
            db,
            min_compatibility_level,
        )
    except Exception as e:
        error_msg = str(e)
        if error_msg.startswith('SQL Server message'):
            error_msg = error_msg.split('\n', 1)[-1]
        if error_msg.startswith('Login failed'):
            logging.warning(error_msg)
            raise CheckException('login failed')

        if 'Previous statement didn\'t produce any results' in error_msg:
            return []
        else:
            raise CheckException(f'query error: {error_msg}')
    else:
        items = []
        for row in rows:
            item = {}
            for colname, val in zip(colnames, row):
                if isinstance(val, datetime.datetime):
                    val = int(val.timestamp())
                elif isinstance(val, decimal.Decimal):
                    val = float(val)
                elif isinstance(val, uuid.UUID):
                    val = str(val)
                item[colname] = val
            try:
                item['name'] = '.'.join(map(str, (item[i] for i in idx)))
            except Exception as e:
                msg = str(e)
                raise CheckException(f'item name error: {msg}')
            items.append(item)
        return items

import asyncio
import datetime
import decimal
import pytds
import logging
import uuid
from libprobe.asset import Asset
from libprobe.exceptions import CheckException
from libprobe.exceptions import IncompleteResultException
from pytds.login import SpnegoAuth
from typing import List, Optional
from . import DOCS_URL
from .asset_cache import AssetCache

APPNAME = 'Infrasonar mssql-probe'
DEFAULT_MSSQL_PORT = 1433


def _get_conn(host, port, username, password, dbname=None):
    auth = SpnegoAuth(username, password) if '\\' in username else None
    return pytds.connect(
        host,
        dbname,
        username,
        password,
        port=port,
        auth=auth,
        appname=APPNAME
    )


def _get_data(asset, host, port, username, password, qry, db, *_):
    with _get_conn(host, port, username, password, db) as conn:
        with conn.cursor() as cur:
            cur.execute(qry)
            res = cur.fetchall()
            collnames = [tup[0] for tup in cur.description]
            return collnames, res


def _get_data_each_db(asset, host, port, username, password, qry, _db,
                      min_level):
    with _get_conn(host, port, username, password) as conn:
        dbs, expired = AssetCache.get_value((asset.id, 'dbnames'))
        if dbs is None or expired:
            dbs = _get_db_names(conn)
            AssetCache.set_value((asset.id, 'dbnames'), dbs, 900)
        noaccess, expired = AssetCache.get_value((asset.id, 'noaccess'))
        if expired:
            noaccess = []
            AssetCache.drop((asset.id, 'noaccess'))
        elif noaccess is None:
            noaccess = []

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
            elif db in noaccess:
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
                    pass
                elif 'is not able to access the database' in msg:
                    noaccess.append(db)
                    AssetCache.set_value((asset.id, 'noaccess'), noaccess,
                                         7200)
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
        idx: List[str] = ['name'],
        db: Optional[str] = None,
        each_db: bool = False,
        min_compatibility_level: Optional[int] = None) -> list:
    address = config.get('address')
    if not address:
        address = asset.name
    username = asset_config.get('username')
    password = asset_config.get('password')
    if username is None or password is None:
        raise CheckException(
            'Missing credentials. Please refer to the following documentation'
            f' for detailed instructions: <{DOCS_URL}>'
        )
    instance = config.get('instance', '')
    if instance:
        address = f'{address}\\{instance}'
        port = None
    else:
        port = config.get('port', DEFAULT_MSSQL_PORT)

    try:
        func = _get_data_each_db if each_db \
            else _get_data
        colnames, rows = await asyncio.get_running_loop().run_in_executor(
            None,
            func,
            asset,
            address,
            port,
            username,
            password,
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
            raise CheckException(f'Query error: {error_msg}')
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
                name = '.'.join(map(str, (item[i] for i in idx)))
                item['name'] = name.encode('ascii', errors='replace').decode()
            except Exception as e:
                msg = str(e)
                raise CheckException(f'Item name error: {msg}')
            items.append(item)
        return items


def check_noaccess(asset: Asset, state: dict):
    noaccess, _ = AssetCache.get_value((asset.id, 'noaccess'))
    if noaccess:
        noaccess = '\n- ' + '\n- '.join(f'`{db}`' for db in noaccess)
        msg = f'Not able to access database(s):{noaccess}'
        raise IncompleteResultException(msg, state)

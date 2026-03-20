from libprobe.asset import Asset
from libprobe.check import Check
from ..mssql_query import get_data
from ..utils import dedup, do_exclude_databases

QUERY = open('lib/query/checkTopQueryIo.sql').read()


class CheckTopQueryIo(Check):
    key = 'topqueryio'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        res = await get_data(asset, local_config, config, QUERY)
        res = do_exclude_databases(res, config)

        return {
            'queryio': dedup(res),
        }

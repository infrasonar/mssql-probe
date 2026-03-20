from libprobe.asset import Asset
from libprobe.check import Check
from ..mssql_query import get_data

QUERY = open('lib/query/checkPlanCache.sql').read()


class CheckPlanCache(Check):
    key = 'plancache'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        res = await get_data(asset, local_config, config, QUERY, db='master')
        return {
            'plancache': res,
        }

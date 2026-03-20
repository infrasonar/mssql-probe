from libprobe.asset import Asset
from libprobe.check import Check
from ..mssql_query import get_data

QUERY = open('lib/query/checkMemoryConsumers.sql').read()
IDX = ['type', 'memory_name']


class CheckMemoryConsumers(Check):
    key = 'memoryconsumers'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        res = await get_data(asset, local_config, config, QUERY, IDX)
        return {
            'memoryconsumers': res,
        }

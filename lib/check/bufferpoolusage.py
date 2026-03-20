from libprobe.asset import Asset
from libprobe.check import Check
from ..mssql_query import get_data
from ..utils import do_exclude_databases

QUERY = open('lib/query/checkBufferPoolUsage.sql').read()


class CheckBufferPoolUsage(Check):
    key = 'bufferpoolusage'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        res = await get_data(asset, local_config, config, QUERY)
        res = do_exclude_databases(res, config, 'name')

        return {
            'bufferpoolusage': res,
        }

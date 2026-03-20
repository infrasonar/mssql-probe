from libprobe.asset import Asset
from libprobe.check import Check
from ..mssql_query import get_data, check_noaccess
from ..utils import dedup_ignore

QUERY = open('lib/query/checkIndexUsage.sql').read()
N = 25


class CheckIndexUsage(Check):
    key = 'indexusage'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        res = await get_data(asset, local_config, config, QUERY, each_db=True)
        top = sorted(res, key=lambda a: a.get('total_usage'), reverse=True)
        state = {
            'indexusage': dedup_ignore(top, N),
        }
        check_noaccess(asset, state)
        return state

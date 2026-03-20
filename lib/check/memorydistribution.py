from libprobe.asset import Asset
from libprobe.check import Check
from ..mssql_query import get_data, check_noaccess
from ..utils import dedup_ignore

QUERY = open('lib/query/checkMemoryDistribution.sql').read()
IDX = ['object_name', 'index_name']
N = 25


class CheckMemoryDistribution(Check):
    key = 'memorydistribution'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        res = await get_data(asset, local_config, config, QUERY, IDX,
                             each_db=True)
        top = sorted(res, key=lambda a: a.get('buffer_size'), reverse=True)
        state = {
            'memorydistribution': dedup_ignore(top, N),
        }
        check_noaccess(asset, state)
        return state

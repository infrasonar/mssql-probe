from libprobe.asset import Asset
from ..mssql_query import get_data, check_noaccess
from ..utils import dedup_ignore

QUERY = open('lib/query/checkMemoryDistribution.sql').read()
IDX = ['object_name', 'index_name']
N = 25


async def check_memorydistribution(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY, IDX, each_db=True)
    top = sorted(res, key=lambda a: a.get('buffer_size'), reverse=True)
    state = {
        'memorydistribution': dedup_ignore(top, N),
    }
    check_noaccess(asset, state)
    return state

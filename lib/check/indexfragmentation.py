from libprobe.asset import Asset
from ..mssql_query import get_data
from ..utils import dedup_ignore

QUERY = open('lib/query/checkIndexFragmentation.sql').read()
IDX = ['database_name', 'schema_name', 'object_name', 'index_name']
N = 25


async def check_indexfragmentation(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY, IDX, each_db=True)
    top = sorted(res, key=lambda a: a.get(
        'avg_fragmentation_in_percent'), reverse=True)[:N]
    return {
        'indexfragmentation': dedup_ignore(top),
    }

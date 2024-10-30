from libprobe.asset import Asset
from ..mssql_query import get_data, check_noaccess
from ..utils import dedup_ignore

QUERY = open('lib/query/checkIndexFragmentation.sql').read()
IDX = ['database_name', 'schema_name', 'object_name', 'index_name']
N = 25


async def check_indexfragmentation(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    # compatilibity level 90 is required for the dm_db_index_physical_stats
    # dynamic view
    res = await get_data(asset, asset_config, config, QUERY, IDX, each_db=True,
                         min_compatibility_level=90)
    top = sorted(res, key=lambda a: a.get(
        'avg_fragmentation_in_percent'), reverse=True)
    state = {
        'indexfragmentation': dedup_ignore(top, N),
    }
    check_noaccess(asset, state)
    return state

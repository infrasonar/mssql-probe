from libprobe.asset import Asset
from ..mssql_query import get_data
from ..utils import dedup_ignore

QUERY = open('lib/query/checkIndexChange.sql').read()
IDX = ['database_name', 'table_name', 'statistic']
N = 25


async def check_indexchange(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    # compatilibity level 90 is required for the using derived arguments when
    # calling the dm_db_stats_properties dynamic view
    res = await get_data(asset, asset_config, config, QUERY, IDX, each_db=True,
                         min_compatibility_level=90)
    top = sorted(res, key=lambda a: a.get('percent_change'), reverse=True)
    return {
        'indexchange': dedup_ignore(top, N),
    }

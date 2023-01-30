from libprobe.asset import Asset
from ..mssql_query import get_data

QUERY = open('lib/query/checkPendingMemoryGrants.sql').read()
IDX = ['server_name', 'object_name']


async def check_pendingmemorygrants(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY, IDX)
    return {
        'grants': res,
    }

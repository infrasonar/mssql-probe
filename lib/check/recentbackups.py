from libprobe.asset import Asset
from ..mssql_query import get_data
from ..utils import dedup

QUERY = open('lib/query/checkRecentBackups.sql').read()
IDX = ['machine_name', 'server_name', 'database_name']


async def check_recentbackups(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY, IDX)
    return {
        'backups': dedup(res),
    }

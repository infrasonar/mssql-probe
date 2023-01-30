from libprobe.asset import Asset
from ..mssql_query import get_data

QUERY = open('lib/query/checkLastBackups.sql').read()
IDX = ['machine_name', 'server_name', 'database_name']


async def check_lastbackups(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY, IDX)
    return {
        'backups': res,
    }

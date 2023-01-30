from libprobe.asset import Asset
from ..mssql_query import get_data

QUERY = open('lib/query/checkSessions.sql').read()
IDX = ['client_net_address', 'program_name', 'host_name', 'login_name']


async def check_sessions(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY, IDX)
    return {
        'sessions': res,
    }

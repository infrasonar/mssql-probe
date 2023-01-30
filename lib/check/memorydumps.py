from libprobe.asset import Asset
from ..mssql_query import get_data

QUERY = open('lib/query/checkMemoryDumps.sql').read()


async def check_memorydumps(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY)
    return {
        'memorydumps': res,
    }

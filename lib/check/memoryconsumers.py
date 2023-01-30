from libprobe.asset import Asset
from ..mssql_query import get_data

QUERY = open('lib/query/checkMemoryConsumers.sql').read()
IDX = ['type', 'memory_name']


async def check_memoryconsumers(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY, IDX)
    return {
        'memoryconsumers': res,
    }

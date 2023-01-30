from libprobe.asset import Asset
from ..mssql_query import get_data
from ..utils import dedup

QUERY = open('lib/query/checkTopWorkerTimeQueries.sql').read()


async def check_topworkertimequeries(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY)
    return {
        'queries': dedup(res),
    }

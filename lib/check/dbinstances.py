from libprobe.asset import Asset
from ..mssql_query import get_data
from ..utils import do_exclude_databases

QUERY = open('lib/query/checkDbInstances.sql').read()


async def check_dbinstances(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY)
    res = do_exclude_databases(res, config)

    return {
        'dbinstances': res,
    }

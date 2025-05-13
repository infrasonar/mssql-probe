from libprobe.asset import Asset
from ..mssql_query import get_data
from ..utils import do_exclude_databases

QUERY = open('lib/query/checkFileLatency.sql').read()


async def check_filelatency(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY, db='master')
    res = do_exclude_databases(res, config)

    return {
        'filelatency': res,
    }

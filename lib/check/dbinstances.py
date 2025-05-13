from libprobe.asset import Asset
from ..mssql_query import get_data

QUERY = open('lib/query/checkDbInstances.sql').read()


async def check_dbinstances(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY)

    exclude_databases = set(
        d.lower() for d in config.get('exclude_databases', []))
    if exclude_databases:
        res = [item for item in res
               if item['database_name'].lower() not in exclude_databases]

    return {
        'dbinstances': res,
    }

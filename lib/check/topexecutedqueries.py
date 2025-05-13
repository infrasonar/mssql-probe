from libprobe.asset import Asset
from ..mssql_query import get_data
from ..utils import dedup

QUERY = open('lib/query/checkTopExecutedQueries.sql').read()


async def check_topexecutedqueries(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY)
    # TODO this queries top 25. exclude database in query?

    exclude_databases = set(
        d.lower() for d in config.get('exclude_databases', []))
    if exclude_databases:
        res = [item for item in res
               if item['database_name'].lower() not in exclude_databases]

    return {
        'topexecutedqueries': dedup(res),
    }

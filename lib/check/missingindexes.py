from libprobe.asset import Asset
from ..mssql_query import get_data

QUERY = open('lib/query/checkMissingIndexes.sql').read()
IDX = ['Database.Schema.Table', 'equality_columns', 'inequality_columns',
       'included_columns']


async def check_missingindexes(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY, IDX)
    return {
        'missingindexes': res,
    }

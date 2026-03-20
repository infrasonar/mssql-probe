from libprobe.asset import Asset
from libprobe.check import Check
from ..mssql_query import get_data

QUERY = open('lib/query/checkMissingIndexes.sql').read()
IDX = ['database_schema_table', 'equality_columns', 'inequality_columns',
       'included_columns']


class CheckMissingIndexes(Check):
    key = 'missingindexes'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        res = await get_data(asset, local_config, config, QUERY, IDX)
        return {
            'missingindexes': res,
        }

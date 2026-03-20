from libprobe.asset import Asset
from libprobe.check import Check
from ..mssql_query import get_data, check_noaccess
from ..utils import dedup_ignore

QUERY = open('lib/query/checkTableSizes.sql').read()
IDX = ['database_name', 'table_name']
N = 25


class CheckTableSizes(Check):
    key = 'tablesizes'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        res = await get_data(asset, local_config, config, QUERY, IDX,
                             each_db=True)
        top = sorted(res, key=lambda a: a.get('row_count'), reverse=True)
        state = {
            'tablesizes': dedup_ignore(top, N),
        }
        check_noaccess(asset, state)
        return state

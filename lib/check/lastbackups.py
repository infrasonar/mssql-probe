from libprobe.asset import Asset
from libprobe.check import Check
from ..mssql_query import get_data
from ..utils import do_exclude_databases

QUERY = open('lib/query/checkLastBackups.sql').read()
IDX = ['machine_name', 'server_name', 'database_name']


class CheckLastBackups(Check):
    key = 'lastbackups'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        res = await get_data(asset, local_config, config, QUERY, IDX)
        res = do_exclude_databases(res, config)

        return {
            'backups': res,
        }

from libprobe.asset import Asset
from libprobe.check import Check
from ..mssql_query import get_data

QUERY = open('lib/query/checkSessions.sql').read()
IDX = ['client_net_address', 'program_name', 'host_name', 'login_name']


class CheckSessions(Check):
    key = 'sessions'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        res = await get_data(asset, local_config, config, QUERY, IDX)
        return {
            'sessions': res,
        }

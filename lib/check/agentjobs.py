from libprobe.asset import Asset
from libprobe.check import Check
from ..mssql_query import get_data
from ..utils import dedup_ignore

QUERY = open('lib/query/checkAgentJobs.sql').read()


class CheckAgentJobs(Check):
    key = 'agentjobs'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        res = await get_data(asset, local_config, config, QUERY)
        return {
            'agentjobs': dedup_ignore(res),
        }

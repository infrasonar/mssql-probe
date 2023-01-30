from libprobe.asset import Asset
from ..mssql_query import get_data
from ..utils import dedup_ignore

QUERY = open('lib/query/checkAgentJobs.sql').read()


async def check_agentjobs(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY)
    return {
        'agentjobs': dedup_ignore(res),
    }

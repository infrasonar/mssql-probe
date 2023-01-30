from libprobe.asset import Asset
from ..mssql_query import get_data

QUERY = open('lib/query/checkPagelifeExpectancy.sql').read()
IDX = ['server_name', 'instance_name']


async def check_pagelifeexpectancy(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY, IDX)
    return {
        'expectancy': res,
    }

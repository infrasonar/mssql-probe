from libprobe.asset import Asset
from ..mssql_query import get_data

QUERY = open('lib/query/checkBestPractices.sql').read()


async def check_bestpractices(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    # TODO in oversight zijn hier geen metrics voor, kan deze check weg?
    res = await get_data(asset, asset_config, config, QUERY)
    return {
        'bestpractices': res,
    }

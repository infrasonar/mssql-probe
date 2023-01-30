from libprobe.asset import Asset
from ..mssql_query import get_data

QUERY = open('lib/query/checkSystem.sql').read()
WINDOWS_SKU_LK = {
    4: 'Enterprise Edition',
    7: 'Standard Server Edition',
    8: 'Datacenter Server Edition',
    10: 'Enterprise Server Edition',
    48: 'Professional Edition'
}


async def check_system(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY)
    for item in res:
        item['windows_sku'] = WINDOWS_SKU_LK.get(item.get('windows_sku'))
    return {
        'system': res,
    }

from libprobe.asset import Asset
from libprobe.check import Check
from ..mssql_query import get_data

QUERY = open('lib/query/checkSystem.sql').read()
WINDOWS_SKU_LK = {
    4: 'Enterprise Edition',
    7: 'Standard Server Edition',
    8: 'Datacenter Server Edition',
    10: 'Enterprise Server Edition',
    48: 'Professional Edition'
}


class CheckSystem(Check):
    key = 'system'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        res = await get_data(asset, local_config, config, QUERY)
        for item in res:
            item['windows_sku'] = WINDOWS_SKU_LK.get(item.get('windows_sku'))
        return {
            'system': res,
        }

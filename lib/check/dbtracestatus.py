from libprobe.asset import Asset
from ..mssql_query import get_data

QUERY = open('lib/query/checkDbTraceStatus.sql').read()
IDX = ['TraceFlag']
BOOL_LK = {
    0: False,
    1: True,
}
STATUS_LK = {
    0: 'Off',
    1: 'On',
}


async def check_dbtracestatus(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY, IDX)
    for item in res:
        item['Global'] = BOOL_LK.get(item['Global'])
        item['Session'] = BOOL_LK.get(item['Session'])
        item['Status'] = STATUS_LK.get(item.get('Status'))

    return {
        'dbtracestatus': res,
    }

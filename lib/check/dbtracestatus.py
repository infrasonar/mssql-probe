from libprobe.asset import Asset
from libprobe.check import Check
from ..mssql_query import get_data

QUERY = open('lib/query/checkDbTraceStatus.sql').read()
BOOL_LK = {
    0: False,
    1: True,
}
STATUS_LK = {
    0: 'Off',
    1: 'On',
}


class CheckDbTraceStatus(Check):
    key = 'dbtracestatus'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        res = await get_data(asset, local_config, config, QUERY, [])
        for item in res:
            item['name'] = str(item.pop('TraceFlag'))
            item['global'] = BOOL_LK.get(item.pop('Global', None))
            item['session'] = BOOL_LK.get(item.pop('Session', None))
            item['status'] = STATUS_LK.get(item.pop('Status', None))

        return {
            'dbtracestatus': res,
        }

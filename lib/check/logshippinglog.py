from libprobe.asset import Asset
from libprobe.check import Check
from ..mssql_query import get_data

QUERY = open('lib/query/checkLogShippingLog.sql').read()
IDX = ['agent_id', 'session_id', 'log_time_utc']
AGENT_TYPE_LK = {
    0: 'Backup',
    1: 'Copy',
    2: 'Restore'
}
STATUS_LK = {
    3: 'Error',
    4: 'Warning'
}


class CheckLogShippingLog(Check):
    key = 'logshippinglog'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        res = await get_data(asset, local_config, config, QUERY, IDX)
        for item in res:
            item['agent_type'] = AGENT_TYPE_LK.get(item.get('agent_type'))
            item['session_status'] = STATUS_LK.get(item.get('session_status'))
        return {
            'log': res,
        }

from libprobe.asset import Asset
from ..mssql_query import get_data

QUERY = open('lib/query/checkDbPerfCounters.sql').read()


async def check_dbperfcounters(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY, [])
    out = {}
    for row in res:
        value = row['cntr_value']
        item_name = row['instance_name']
        if item_name not in out:
            out[item_name] = {'name': item_name}
        metric_name = row['counter_name'] \
            .strip() \
            .lower() \
            .replace(' ', '_') \
            .replace('/sec', '')
        if metric_name.endswith('_ratio'):
            metric_name = metric_name[:-6]
        out[item_name][metric_name] = value

    return {
        'dbperf': tuple(out.values()),
    }

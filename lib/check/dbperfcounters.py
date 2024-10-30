from libprobe.asset import Asset
from ..mssql_query import get_data
from ..utils import perf_large_raw_fraction

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
        out[item_name][metric_name] = value

    for item in out.values():
        perf_large_raw_fraction('cache_hit_ratio', item)

    return {
        'dbperf': tuple(out.values()),
    }

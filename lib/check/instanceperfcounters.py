import asyncio
from libprobe.asset import Asset
from ..mssql_query import get_data
from ..utils import perf_average_bulk, perf_large_raw_fraction

_CACHE = {}
QUERY = open('lib/query/checkInstancePerfCounters.sql').read()


def on_data(res):
    item = {'name': 'system'}
    for row in res:
        metric_name = row['counter_name'] \
            .strip() \
            .lower() \
            .replace('(timeout > 0)', 'timeout_gt_0') \
            .replace(' ', '_') \
            .replace('-', '_') \
            .replace('/sec', '')

        val = row['cntr_value']
        if metric_name.endswith('_(ms)'):
            metric_name = metric_name[:-5]
            val = val / 1000

        if metric_name == 'average_wait_time_base':
            val = val / 1000

        if metric_name in item:
            raise Exception(
                f'Duplicate metric: {metric_name}: '
                f'{val} vs {item[metric_name]}')
        item[metric_name] = val
    return item


async def check_instanceperfcounters(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY, [])
    item = on_data(res)

    prev = _CACHE.get(asset.id)
    if prev is None:
        prev = item
        await asyncio.sleep(3)
        res = await get_data(asset, asset_config, config, QUERY, [])
        item = on_data(res)

    # store a copy as we will alter the item for a compact result
    _CACHE[asset.id] = item.copy()

    perf_average_bulk('average_wait_time', item, prev)
    perf_average_bulk('update_conflict_ratio', item, prev)
    perf_large_raw_fraction('buffer_cache_hit_ratio', item)

    return {
        'instanceperf': [item],
    }

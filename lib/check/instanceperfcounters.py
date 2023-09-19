from libprobe.asset import Asset
from ..mssql_query import get_data

QUERY = open('lib/query/checkInstancePerfCounters.sql').read()


async def check_instanceperfcounters(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY, [])
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

        if metric_name in item:
            raise Exception(
                f'Duplicate metric: {metric_name}: '
                f'{val} vs {item[metric_name]}')
        item[metric_name] = val

    n = item.pop('buffer_cache_hit_ratio', None)
    base = item.pop('buffer_cache_hit_ratio_base', None)
    if None not in (n, base):
        try:
            item['buffer_cache_hit_ratio'] = n / base
        except ZeroDivisionError:
            pass

    n = item.pop('update_conflict_ratio', None)
    base = item.pop('update_conflict_ratio_base', None)
    if None not in (n, base):
        try:
            item['update_conflict'] = n / base
        except ZeroDivisionError:
            pass

    return {
        'instanceperf': [item],
    }

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
            .replace(' ', '_') \
            .replace('-', '_') \
            .replace('/sec', '')
        if metric_name.endswith('_ratio'):
            metric_name = metric_name[:-6]

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

    return {
        'instanceperf': [item],
    }

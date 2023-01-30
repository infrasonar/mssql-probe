import re
from collections import Counter
from libprobe.asset import Asset
from ..mssql_query import get_data

QUERY = open('lib/query/checkApplicationSessions.sql').read()
UUID_RE = re.compile('([0-9a-f]{4,}-)+[0-9a-f]{4,}', re.IGNORECASE)


async def check_applicationsessions(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY)
    counts = {}
    block_sources = {}
    victim_count = 0
    for item in res:
        if len(item['blk_by']) > 1:
            victim_count += 1
            block_source = \
                item['database_name'] + '-' + item['blk_by']
            if block_source not in block_sources:
                block_sources[block_source] = {
                    'name': block_source,
                    'victims': 0,
                    'database_name': item['database_name'],
                    'command': item['command'],
                    'login': item['login'],
                    'program_name': item['program_name'],
                    'status': item['status'],
                    'spid_1': item['spid_1']
                }
            block_item = block_sources[block_source]
            block_item['victims'] += 1

        program_name = item['program_name']
        program_name = UUID_RE.sub('', program_name) \
            if program_name else program_name
        if program_name in counts:
            cur_counts = counts[program_name]
        else:
            counts[program_name] = cur_counts = {
                'cpu_time': 0.0,
                'disk_io': 0,
                'logins': Counter(),
                'host_names': Counter()
            }

        cur_counts['cpu_time'] += item['cpu_time'] \
            if item['cpu_time'] > 0 else 0
        cur_counts['disk_io'] += item['disk_io']
        cur_counts['logins'][item['login']] += 1
        cur_counts['host_names'][item['host_name']] += 1

    for item_name in counts:
        item = counts[item_name]
        item['name'] = item_name
        item['sessions'] = sum(v for v in item['logins'].values())
        item['hosts'] = len(set(item.pop('host_names')))
        item['accounts'] = len(set(item.pop('logins')))

    return {
        'applications': list(counts.values()),
        'blocks': list(block_sources.values()),
        'blockcount': [{'name': 'victims', 'victims': victim_count}]
    }

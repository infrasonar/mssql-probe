from collections import Counter


def dedup(items: list) -> list:
    counts = Counter()
    for item in items:
        name = item['name']
        if counts[name]:
            item['name'] = f'{name}_{counts[name]}'
        counts[name] += 1
    return items


def dedup_ignore(items: list, max_items=None) -> list:
    names = set()
    new = []
    for item in items:
        name = item['name']
        if name in names:
            continue
        names.add(name)
        new.append(item)
        if max_items is not None and len(new) == max_items:
            break
    return new


def perf_average_bulk(metric_name: str, item: dict, prev: dict):
    # cntr_type 1073874176
    n0 = prev.get(metric_name)
    n1 = item.pop(metric_name, None)
    d0 = prev.get(f'{metric_name}_base')
    d1 = item.pop(f'{metric_name}_base', None)
    try:
        assert n1 - n0 > 0
        item[metric_name] = (n1 - n0) / (d1 - d0)
    except AssertionError:
        item[metric_name] = 0.0
    except Exception as e:
        pass


def perf_large_raw_fraction(metric_name: str, item: dict):
    # cntr_type 537003264
    n = item.pop(metric_name, None)
    d = item.pop(f'{metric_name}_base', None)
    try:
        assert n > 0
        item[metric_name] = n / d * 100.0
    except AssertionError:
        item[metric_name] = 0.0
    except Exception as e:
        pass

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

from collections import Counter


def dedup(items: list) -> list:
    counts = Counter()
    for item in items:
        name = item['name']
        item['name'] = f'{name}_{counts[name]}'
        counts[name] += 1
    return items


def dedup_ignore(items: list) -> list:
    names = set()
    new = []
    for item in items:
        name = item['name']
        if name in names:
            continue
        names.add(name)
        new.append(item)
    return new

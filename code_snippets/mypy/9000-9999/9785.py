import collections
import re

PATTERN = re.compile('^([^ ]+ [^ ]+) bags contain (.*)$')
BAG_RE = re.compile(r'(\d+) ([^ ]+ [^ ]+)')


def compute(s: str) -> int:
    parents = collections.defaultdict(list)
    for line in s.splitlines():
        match = PATTERN.match(line)
        assert match
        k = match[1]
        targets = [(int(n), tp) for n, tp in BAG_RE.findall(match[2])]
        for _, color in targets:
            parents[color].append(k)

    total_colors = set()
    todo = parents['shiny gold']
    while todo:
        color = todo.pop()
        if color not in total_colors:
            total_colors.add(color)
            todo.extend(parents[color])

    reveal_type(parents)

    return len(total_colors)

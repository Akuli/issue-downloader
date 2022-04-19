a = defaultdict(list)
a[0].append('yes')

b = {}
b.setdefault(0, []).append('yes')

c = defaultdict(set)
c[0].add('yes')

d = {}
d.setdefault(0, set()).add('yes')

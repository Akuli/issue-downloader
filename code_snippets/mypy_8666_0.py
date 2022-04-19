import itertools
itertools.starmap(
    lambda x, y: True, filter(lambda in_deg: in_deg[1],
                              [(1, 2)]))

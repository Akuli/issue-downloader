z1 = list(zip((1, 10), (2, 20), (3, 30)))  # correct: list[Tuple[int, int, int]]
z2 = list(zip(*[(1, 10), (2, 20), (3, 30)]))  # list[tuple[Any, ...]] but I expect list[tuple[int, int, int]]

# Currently supported:
SboxType = Tuple[
    Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int],
    Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int],
    Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int],
    Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int],
    Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int],
    Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int],
    Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int],
    Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int],
]

# Proposed:
SboxType = Tuple[Tuple[int, 16], 8] # A tuple of 8 tuples of 16 ints each

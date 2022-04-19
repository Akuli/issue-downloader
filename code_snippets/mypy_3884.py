from typing import Tuple, Dict
from itertools import product

# works fine
XY_1: Dict[str, Tuple[int, int]] = dict(zip('abcd', product(range(2), range(2))))
# {'a': (0, 0), 'b': (0, 1), 'c': (1, 0), 'd': (1, 1)}

# error for this one
XY_2: Dict[str, Tuple[int, int]] = dict(zip('abcd', product(range(2), repeat=2)))
# {'a': (0, 0), 'b': (0, 1), 'c': (1, 0), 'd': (1, 1)}

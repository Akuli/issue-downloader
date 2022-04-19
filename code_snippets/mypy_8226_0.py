import itertools
from typing import List

x: List[int] = [1, 2, 3]
y: List[str] = ["  ", "", "abc"]


it = itertools.chain(x, filter(lambda s: s.strip() == "", y))
reveal_type(it)

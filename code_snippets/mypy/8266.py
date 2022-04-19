from typing import List, NoReturn, Sequence

a: List[List[int]] = [] # ok
b: List[NoReturn] = [] # ok
c: List[List[NoReturn]] = [[]] # ok
d: List[List[NoReturn]] = [[]][:0] # ok
e: List[List[NoReturn]] = [] # error
f: Sequence[List[NoReturn]] = [] # ok

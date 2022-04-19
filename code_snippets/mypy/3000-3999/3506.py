from typing import *
T = TypeVar('T')
def f(a: Union[List[int], T]) -> T: pass
f([1])  # OK
f([''])  # E: List item 0 has incompatible type "str"   <<--- unexpected
a = ['']
f(a)  # OK

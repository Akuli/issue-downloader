from typing import *
U = Union[int, str]
d: Dict[Type[U], int] = {int: 1, str: 2}
T = TypeVar('T', bound=U)
def get(t: Type[T]) -> int:
    return d[t]

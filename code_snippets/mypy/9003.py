def f(t: Type[T]) -> T: ...

from typing import *
from dataclasses import dataclass
T = TypeVar('T')

@dataclass
class P:
    a: int

class Q(NamedTuple):
    a: int

def create(t: Type[T]) -> T:    ...

# These ones work
reveal_type(create(int))
reveal_type(create(str))
reveal_type(create(List[int]))
reveal_type(create(Dict[int, int]))
reveal_type(create(Q))
reveal_type(create(P))

# These do not
reveal_type(create(Tuple[int]))
reveal_type(create(Union[int,str]))
reveal_type(create(Optional[int]))


from typing import Set, FrozenSet, List, Tuple
from typing_extensions import Literal

T = Literal[1, 2, 3]
l: List[T] = [1, 2]
t1: Tuple[T, ...] = (1, 2)
t2: Tuple[T, T] = (1, 2)
s1: Set[T] = {1, 2}
s2: Set[T] = set([1, 2])
s3: Set[int] = set((1, 2))
f1: FrozenSet[T] = frozenset([1, 2])
f2: FrozenSet[int] = frozenset((1, 2))
# no error on any of the above

s4: Set[T] = set((1, 2))
# error: Argument 1 to "set" has incompatible type "Tuple[int, int]"; expected "Iterable[Union[Literal[1], Literal[2], Literal[3]]]"

f3: FrozenSet[T] = frozenset((1, 2))
# error: Argument 1 to "frozenset" has incompatible type "Tuple[int, int]"; expected "Iterable[Union[Literal[1], Literal[2], Literal[3]]]"

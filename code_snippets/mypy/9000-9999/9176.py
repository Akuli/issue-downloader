from itertools import chain
from typing import List


ints_of_ints: List[List[int]]
c = filter(lambda ints: len(ints), ints_of_ints)  # ok
reveal_type(c)  # typing.Iterator[builtins.list[builtins.int]]

d = chain.from_iterable(filter(lambda ints: len(ints), ints_of_ints))  # mypy: error arg-type - Argument 1 to "len" has incompatible type
                                                                       # "Iterable[int]"; expected "Sized"
reveal_type(d)  # typing.Iterator[builtins.int*]

from typing import Optional
from typing import Sequence

from more_itertools import first


class A:
    def some_method(self):
        pass


def f(inp: Sequence[A]) -> Optional[A]:
    return first(filter(lambda a: a.some_method(), inp), None)

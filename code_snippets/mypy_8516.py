from typing import Any, Generic, Callable, TypeVar

T = TypeVar('T')

class lazy:
    def __init__(self, func: Callable[[Any], T]) -> None: ...
    def __get__(self, inst: Any, inst_cls: Any) -> T: ...

class Haystack:
    @lazy
    def hasNeedles(self) -> bool:
        # some expensive lookup we want to execute only once
        return True

reveal_type(Haystack().hasNeedles)

# checking this expression crashes
x = Haystack().hasNeedles or True

def lazy(func: Callable[[Any], T]) -> T: ...


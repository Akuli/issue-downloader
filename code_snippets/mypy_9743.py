from typing import (
    Generic,
    TypeVar,
)
_MyType = TypeVar("_MyType", str, float) 

class MyGeneric(Generic[_MyType]):
    def __init__(self, attr: int) -> None:
        ls = [0]
        self.attr = attr          # mypy says: error: Need type annotation for 'attr'
        if (a := sum(ls)): # mypy says: error: Cannot determine type of 'ls'
            pass
        reveal_type(ls)        # mypy says: note: Revealed type is 'builtins.list[builtins.int*]'

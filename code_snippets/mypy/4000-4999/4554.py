# Run with --strict-optional
from typing import TypeVar, Callable, Optional, List
_T = TypeVar('_T')
def make(typ: Callable[[], _T]) -> _T:
    ...
def accept(arg: Optional[_T]) -> _T:
    ...
accept(make(list))
accept(None)
foo = accept(make(list))                   # This works
bar: List[str] = accept(make(list))    # Argument 1 to "accept" has incompatible type "List[_T]"; expected "Optional[List[str]]"

import attr
x: List[str] = attr.ib(attr.Factory(list))

from typing import Any, Callable, Type, TypeVar, Union, cast

_T = TypeVar("_T")

class Cls: ...
def wrap(decorator: Callable[[_T], _T]) -> Callable[[_T], _T]: ...

s: Callable[[_T], _T]
w = wrap(s)

s(Cls)
w(Cls)  # error: Argument 1 has incompatible type "Type[Cls]"; expected "_T"

reveal_type(s)
reveal_type(w)

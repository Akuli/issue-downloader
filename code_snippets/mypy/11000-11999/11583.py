from typing import Any, Optional, TypeVar

_T = TypeVar('_T')

def f(b: bool = True, **kwargs: Any) -> None:
    pass

def g(x: _T) -> _T:
    f(**{'x': x})
    return x

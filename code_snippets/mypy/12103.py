# test_case.py
from __future__ import annotations
from functools import wraps
from typing import Callable, Optional, Protocol, TypeVar, Union, overload

_ReturnsIntT = Callable[..., int]
_SubjectT = TypeVar("_SubjectT", bound=_ReturnsIntT)

class _DecoratedT(Protocol):
    def __call__(self, *args: int, join_str="", **kw: int) -> str:
        ...

@overload
def strintify(
    *,
    addtl: Union[int, _SubjectT] = 0,
) -> Callable[[_SubjectT], _DecoratedT]:
    ...

@overload
def strintify(
    f: _SubjectT,
) -> _DecoratedT:
    ...

def strintify(
    f: Optional[_SubjectT] = None,
    *,
    addtl: Union[int, _SubjectT] = 0,
) -> Union[Callable[[_SubjectT], _DecoratedT], _DecoratedT]:
    assert callable(f) or f is None

    def _decorator(f):
        @wraps(f)
        def _f(*args: int, join_str="", **kw: int) -> str:
            res = [f(*args, **kw)]
            if isinstance(addtl, int):
                res[0] += addtl
            else:
                res.append(addtl(*args, **kw))
            return join_str.join(str(i) for i in res)

        return _f
    return _decorator(f) if callable(f) else _decorator

@strintify  # <-- this is fine
def func1(a: int, b: int, c: int) -> int:
    return a**3 + b**2 + c

print(func1(3, 2, 1))  # prints 32
print(func1(3, 2, 1, join_str="|"))  # prints 32

@strintify(addtl=1)  # <-- #@#@#@#@# ERRORS HERE #@#@#@#@#
def func2(a: int, b: int, c: int) -> int:
    return a**3 + b**2 + c

print(func2(3, 2, 1))  # prints 33
print(func2(3, 2, 1, join_str="|"))  # prints 33

@strintify(addtl=lambda a, b, c: c**3 + b**2 + a)  # <-- this is fine
def func3(a: int, b: int, c: int) -> int:
    return a**3 + b**2 + c

print(func3(3, 2, 1))  # prints 328
print(func3(3, 2, 1, join_str="|"))  # prints 32|8

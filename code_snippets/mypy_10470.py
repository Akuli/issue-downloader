from collections import namedtuple
from typing import Any, Callable, cast, Dict, List, NamedTuple, overload, TypeVar, Union

F = TypeVar("F", bound=Callable[..., Any])
Arg: NamedTuple = namedtuple("Arg", ["arg"])


class Test:
    @overload
    def __call__(self, fn: F) -> F:
        ...

    @overload
    def __call__(self, *args: Any, **kwargs: Any) -> "Test":
        ...

    def __call__(self, *args: Any, **kwargs: Any) -> Union[F, "Test"]:
        if len(args) == 1:
            return cast(F, args[0])

        return self

reveal_type(Test()(Test))



def broken(arg: Arg) -> Arg:
    return arg

reveal_type(broken)
reveal_type(Test()(broken))



def working(arg: int) -> int:
    return arg

reveal_type(Test()(working))



@overload
def overloaded_broken(arg: F) -> F:
    ...

@overload
def overloaded_broken(*args: Any, **kwargs: Any) -> Dict[str, int]:
    ...

def overloaded_broken(*args: Any, **kwargs: Any) -> Union[F, Dict[str, int]]:
    if len(args) == 1:
        return cast(F, args[0])

    return dict(args=len(args), kwargs=len(kwargs))


reveal_type(overloaded_broken)
reveal_type(Test()(overloaded_broken))


@overload
def overloaded_working(arg: str) -> str:
    ...

@overload
def overloaded_working(arg: bytes) -> bytes:
    ...

def overloaded_working(arg: Union[bytes, str]) -> Union[bytes, str]:
    return arg


reveal_type(Test()(overloaded_working))

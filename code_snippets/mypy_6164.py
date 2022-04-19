from typing import Callable, Tuple, TypeVar, Iterator, Any, overload

T1 = TypeVar("T1")
T2 = TypeVar("T2")
S = TypeVar("S")

@overload
def star(f: Callable[[T1], S]) -> Callable[[Tuple[T1]], S]: ...

@overload
def star(f: Callable[[T1, T2], S]) -> Callable[[Tuple[T1, T2]], S]: ...

def star(f: Any) -> Any:
    def wraps(tup: Tuple[Any, ...]) -> Any:
        return f(*tup)
    return wraps

def test() -> None:
    values = ["one", "two", "three", "four"]
    pred = lambda _idx, val: bool(val)
    filter(star(lambda _idx, val: bool(val)), enumerate(values))
    filter(star(pred), enumerate(values))

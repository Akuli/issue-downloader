from typing import (
    Callable,
    TypeVar,
    Union,
    Tuple,
)


T = TypeVar("T")


def test(pred: Callable[[T], bool]) -> Tuple[Union[T, int]]:
    return (1,)


def main(pred: Callable[[T], bool]) -> None:
    (val,) = test(pred)  # the error appears here


def f(x: int) -> bool:
    return x > 1


main(f)

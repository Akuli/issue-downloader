from __future__ import annotations
import typing as t


@t.overload
def func2(a: int,
          b: str,
          x: t.Callable[[int], int],
          y: t.Callable[[str], int]) -> tuple[int, int]: ...
@t.overload
def func2(a: int,
          b: str,
          x: t.Callable[[t.Union[int, str]], int]) -> tuple[int, int]: ...


def func2(a: int,
          b: str,
          x: t.Callable[[int], int],
          y: t.Optional[t.Callable[[str], int]] = None):
    y = y or x
    return x(a), y(b)


@t.overload
def func3(a: int,
          b: str,
          x: t.Callable[[int], int],
          y: t.Callable[[str], int]) -> tuple[int, int]: ...
@t.overload
def func3(a: int,
          b: str,
          x: t.Callable[[t.Union[int, str]], int]) -> tuple[int, int]: ...


def func3(a: int,
          b: str,
          x: t.Union[t.Callable[[int], int], t.Callable[[t.Union[int, str]], int]],
          y: t.Optional[t.Callable[[str], int]] = None):
    if y:
        y2 = y
    else:
        y2 = x
    return x(a), y2(b)


@t.overload
def func4(a: int,
          b: str,
          x: list[int],
          y: list[str]): ...
@t.overload
def func4(a: int,
          b: str,
          x: list[t.Union[int, str]]): ...


def func4(a: int,
          b: str,
          x: t.Union[list[int], list[t.Union[int, str]]],
          y: t.Optional[list[str]] = None):
    if y:
        y2 = y
    else:
        y2 = x
    x.append(a)
    y2.append(b)

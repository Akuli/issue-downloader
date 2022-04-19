from __future__ import annotations

from typing import (
    Callable,
    Literal,
    TypeVar,
    overload,
)

F = TypeVar("F", bound=Callable)


def deprecate() -> Callable[[F], F]:
    ...


NDFrameT = TypeVar("NDFrameT", bound="NDFrame")


class NDFrame:
    @overload
    def drop(self, inplace: Literal[True]) -> None:
        ...

    @overload
    def drop(self: NDFrameT, inplace: Literal[False]) -> NDFrameT:
        ...

    @deprecate()
    def drop(self: NDFrameT, inplace: bool) -> NDFrameT | None:
        ...


class Series(NDFrame):
    @overload
    def drop(self, inplace: Literal[True]) -> None:
        ...

    @overload
    def drop(self, inplace: Literal[False]) -> Series:
        ...

    @deprecate()  # removing this decorator avoids the error
    def drop(self, inplace: bool) -> Series | None:
        ...

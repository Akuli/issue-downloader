from typing import TypeVar

Self = TypeVar("Self")

class Flag:
    def __or__(self: Self, other: Self) -> Self: ...
    __ror__ = __or__

class IntFlag(int, Flag):
    def __or__(self: Self, other: int) -> Self: ...
    def __ror__(self: Self, other: int) -> Self: ...

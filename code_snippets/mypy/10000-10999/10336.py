from __future__ import annotations
from typing import overload


class Money:
    @overload
    def __init__(self, amount: object = ..., *, currency: str) -> None:
        ...

    @overload
    def __init__(self, amount: object, currency: str) -> None:
        ...

    def __init__(
        self,
        amount: object = 0,
        currency: str | None = None
    ) -> None:
        if currency is None:
            raise TypeError(
                "__init__() missing 1 required positional argument: 'currency'"
            )

from repr import Money
Money(1)

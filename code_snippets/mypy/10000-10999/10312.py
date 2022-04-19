from __future__ import annotations
from typing import Any, Generic, TypeVar, overload, List
from typing_extensions import Literal


_T = TypeVar("_T")


class ListField(Generic[_T]):
    @overload
    def __init__(
        self: ListField[int],
        *,
        kind: Literal["integer"],
    ) -> None:
        ...

    @overload
    def __init__(
        self: ListField[str],
        *,
        kind: Literal["string"],
    ) -> None:
        ...

    def __init__(self, *, kind: Any) -> None:
        ...

    @overload
    def __get__(
        self: ListField[int],
        instance: Any,
        owner: Any,
    ) -> List[int]:
        ...

    @overload
    def __get__(
        self: ListField[str],
        instance: Any,
        owner: Any,
    ) -> List[str]:
        ...

    def __get__(self: Any, instance: Any, owner: Any) -> Any:
        ...


class Audience:
    usernames = ListField(kind="string")
    ages = ListField(kind="integer")


audience = Audience()
reveal_type(audience.usernames)  # Revealed type is list[int]
reveal_type(audience.ages)  # Revealed type is list[int]


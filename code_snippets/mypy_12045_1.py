# related_field_minimal.pyi
from typing import Generic, Literal, Optional, Type, TypeVar, overload

class Model: ...

_M = TypeVar("_M", bound=Optional[Model])

class ForeignKey(Generic[_M]):
    @overload
    def __new__(
        cls,
        to: Type[_M],
        null: Literal[False] = ...,
    ) -> ForeignKey[_M]: ...
    @overload
    def __new__(
        cls,
        to: Type[_M],
        null: Literal[True],
    ) -> ForeignKey[Optional[_M]]: ...
    def __init__(self, to: Type[_M], null: bool) -> None: ...

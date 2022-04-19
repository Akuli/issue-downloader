from typing import Any
from typing import Protocol
from typing import runtime_checkable
from typing import Type
from typing import TypeVar
from typing import Union

T = TypeVar("T", bound=Any)


@runtime_checkable
class Parsable(Protocol):
    @classmethod
    def parse(cls: Type[T], data: Any) -> T:
        ...


R = TypeVar("R", bound=Union[Parsable, str])


def parse_object(response_type: Type[R], item: Any) -> R:
    if issubclass(response_type, Parsable):
        # note: Revealed type is 'Type[reproduce-issubclass-bug.Parsable]'
        reveal_type(response_type)
        # error: Incompatible return value type (got "Parsable", expected "R")
        return response_type.parse(item)
    # note: Revealed type is 'Type[R`-1]'
    reveal_type(response_type)
    # error: Too many arguments for "Parsable"
    # error: Incompatible return value type (got "Union[Parsable, str]", expected "R")
    return response_type(item)

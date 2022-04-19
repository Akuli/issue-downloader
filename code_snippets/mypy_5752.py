from typing import Type, Union
from typing_extensions import Protocol


class HasFoo(Protocol):
    # foo: str            # works
    foo: Union[str, int]  # fails


def dec(cls: Type[HasFoo]) -> Type[HasFoo]:
    return cls


@dec
class Thing:
    foo = 'abc'

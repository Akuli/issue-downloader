import typing
import typing_inspect

T = typing.TypeVar("T")

class Inst(typing.Generic[T]):
    @classmethod
    def hi(cls):
        return cls

from typing import Generic, TypeVar

T_co = TypeVar("T_co", covariant=True)


class C(Generic[T_co]):
    def __init__(self, x: T_co) -> None:
        ...

    @classmethod
    def custom_init(cls, x: T_co) -> "C[T_co]":
        # error: Cannot use a covariant type variable as a parameter
        return cls(x)

T_cov = typing.TypeVar("T_cov", covariant=True)

class ListProtocol(typing_extensions.Protocol[T_cov]):
    @classmethod
    def create(cls, *items: T_cov) -> "ListProtocol[T_cov]":
        ...

    def getitem(self) -> T_cov:
        ...
    
    ...


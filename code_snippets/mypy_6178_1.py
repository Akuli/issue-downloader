T_cov = typing.TypeVar("T_cov", covariant=True)

class ListProtocol(typing_extensions.Protocol[T_cov]):
    @classmethod
    def create(cls, *items: T_cov) -> "ListProtocol[T_cov]":
        ...

    def getitem(self) -> T_cov:
        ...
    
    ...

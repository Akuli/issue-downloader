from dataclasses import dataclass
from typing import Protocol, Dict, TypeVar, Generic


class DataclassProtocol(Protocol):
    __dataclass_fields__: Dict


T = TypeVar("T", bound=DataclassProtocol)


@dataclass
class MyDataclass:
    x: int = 1


class MyGeneric(Generic[T]):
    ...


class MyClass(MyGeneric[MyDataclass]):
    ...


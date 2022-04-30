from dataclasses import dataclass
from typing import Any, TypeVar

T = TypeVar('T', bound='X')
U = TypeVar('U', bound='Y')
V = TypeVar('V', bound='Z')

@dataclass
class X:
    @classmethod
    def factory(cls: type[T], **kwargs: Any) -> T:
        return cls(**kwargs)

@dataclass
class Y(X):
    y: int

    @classmethod
    def factory(cls: type[U], **kwargs: Any) -> U:
        return super().factory(y=0, **kwargs)

@dataclass
class Z(X):
    z: int

    @classmethod
    def factory(cls: type[V], **kwargs: Any) -> V:
        return super().factory(z=0, **kwargs)

class W(Y, Z):
    pass

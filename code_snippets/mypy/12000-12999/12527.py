import dataclasses
from typing import Generic, TypeVar

T = TypeVar("T", bound="NotDefined")

@dataclasses.dataclass
class C(Generic[T]):
    x: float

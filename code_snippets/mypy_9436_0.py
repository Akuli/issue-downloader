from typing import Protocol, TypeVar, Generic

# Define a protocol for `__radd__`
T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)

class SupportsRAdd(Protocol[T_contra, T_co]):
    def __radd__(self, other: T_contra) -> T_co: ...

from typing import Protocol, overload, TypeVar

# Step 1: Define the class
class ndarray:
    @overload
    def argmax(self, axis: None) -> int: ...
    @overload
    def argmax(self, axis: int) -> ndarray: ...


# Step 2: Define a Protocol for describing the classes' argmax method
T_contra = TypeVar("T_contra", contravariant=True)
T_co = TypeVar("T_co", covariant=True)

class SupportsArgmax(Protocol[T_contra, T_co]):
    def argmax(self, axis: T_contra) -> T_co: ...


# Step 3: Define a wrapper function around the classes' argmax method
T1 = TypeVar("T1")
T2 = TypeVar("T2")

def argmax(a: SupportsArgmax[T1, T2], axis: T1) -> T2: ...


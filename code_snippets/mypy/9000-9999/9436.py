from typing import Protocol, TypeVar, Generic

# Define a protocol for `__radd__`
T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)

class SupportsRAdd(Protocol[T_contra, T_co]):
    def __radd__(self, other: T_contra) -> T_co: ...

class generic: ...  # baseclass for numpy scalars

T1 = TypeVar("T1", bound=generic)
T2 = TypeVar("T2", bound=generic)

class bool_(generic):
    def __radd__(self, other: T1) -> T1: ...
    def __add__(self, other: T1) -> T1: ...

class ndarray(Generic[T1]):
    def __add__(self, other: SupportsRAdd[T1, T2]) -> ndarray[T2]: ...


array: ndarray[bool_]
scalar: bool_

# note: Revealed type is 'op.bool_*'
reveal_type(scalar + scalar)

# error: Value of type variable "T1" of "__radd__" of "bool_" cannot be "ndarray[bool_]"  [type-var]
# note: Revealed type is 'op.ndarray*[op.bool_]'
reveal_type(array + scalar)


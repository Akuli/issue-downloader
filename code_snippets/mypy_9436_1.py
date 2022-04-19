class generic: ...  # baseclass for numpy scalars

T1 = TypeVar("T1", bound=generic)
T2 = TypeVar("T2", bound=generic)

class bool_(generic):
    def __radd__(self, other: T1) -> T1: ...
    def __add__(self, other: T1) -> T1: ...

class ndarray(Generic[T1]):
    def __add__(self, other: SupportsRAdd[T1, T2]) -> ndarray[T2]: ...

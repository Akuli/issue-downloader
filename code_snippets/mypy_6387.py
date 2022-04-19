Types = Union[int, str]
T = TypeVar('T', bound=Types)

class A:
    x: Types
    y: Type[Types]

class B(A, Generic[T]):
    x: T        # ok
    y: Type[T]  # error: Incompatible types in assignment

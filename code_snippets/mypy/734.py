T = TypeVar('T', covariant=True)
class A(Generic[T]):
    def foo(self, x: T) -> None: ...  # Can't use as argument type! Return type is okay.

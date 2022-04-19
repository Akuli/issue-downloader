T = TypeVar('T')

class MyClass(Generic[T]):
    def meth_1(self, x: T) -> T: ...

T = TypeVar("T", bound=A)

class Foo(Generic[T]):
     pass

FooB = Foo[B]

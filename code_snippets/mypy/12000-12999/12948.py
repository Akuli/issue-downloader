T = TypeVar('T')
S = TypeVar('S')


class Foo(Generic[T]):
    pass


def f(x: T) -> None:
    y: Foo[T] = Foo[T]()
    z = Foo[S]()
    # Type variable "S" is unbound
    # z: Foo[S] = Foo[S]()
    reveal_locals()

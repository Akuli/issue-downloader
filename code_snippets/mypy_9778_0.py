T = typing.TypeVar("T")

def callable_or_raise(foo: T) -> T:
    if foo and not callable(foo):
        raise ValueError("bad!")
    return foo

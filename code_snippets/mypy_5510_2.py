class Dummy(Generic[T]): pass

@overload
def f3(d: Dummy[T], x: int) -> int: ...
@overload
def f3(d: Dummy[T], x: T) -> T: ...
def f3(*args, **kwargs): pass

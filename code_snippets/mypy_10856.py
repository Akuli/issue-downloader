...

_a = make_fun('a')
_b = make_fun('b')

@overload
def a(s: int) -> int: ...
@overload
def a(s: str) -> str: ...

def a(s: T) -> T:
    return _a(s)

@overload
def b(s: int) -> int: ...
@overload
def b(s: str) -> str: ...

def b(s: T) -> T:
    return _b(s)

def f(a: int) -> None: pass

x = [1, 2]
f(*x)  # Currently accepted, since mypy doesn't know the length of x

x = [1, 2]
a, b, c = x  # Currently accepted

def f(a: int, b: int) -> None: pass

def g(x: List[int]) -> None:
    assert len(x) == 2
    f(x[0], x[1])


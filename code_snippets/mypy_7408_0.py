def f(a: int) -> None: pass

x = [1, 2]
f(*x)  # Currently accepted, since mypy doesn't know the length of x

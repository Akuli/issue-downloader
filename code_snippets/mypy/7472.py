def deco(x): return x

@deco   # Error: Name 'bad' is not defined
def f(y):
    # type: (bad) -> None
    pass

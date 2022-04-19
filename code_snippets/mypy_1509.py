def f() -> None:
    return g()   # oops, but no error

def g():
    return 1

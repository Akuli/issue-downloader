x = None

def f() -> None:
    reveal_type(x)  # None
    if x:
        1()  # No error, considered as not reachable
        y = 1
    else:
        y = ''  # No error

x = 1
reveal_type(x)  # int

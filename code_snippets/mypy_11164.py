def func() -> bool:
    return True

if not func:
    a: str = 4
    reveal_type(a)
else:
    b: str = 4
    reveal_type(b)

if func:
    c: str = 4
    reveal_type(c)
else:
    d: str = 4
    reveal_type(d)

def foo(cond: bool) -> None:
    if cond:
        a: Final = Funny("spam")
    else:
        a: Final = Funny("eggs")  # this is currently an error

def foo(cond: bool) -> None:
    a: Final[Funny]
    if cond:
        a = Funny("spam")
    else:
        a = Funny("eggs")

def foo(cond: bool) -> None:
    a: Final = Funny("spam") if cond else Funny("eggs")

def foo() -> None:
    for i in [1,2,3]:
        a: Final = i * 2  # currently an error
        a = 10  # error
        print(a)
    print(a)
    a = 10  # error

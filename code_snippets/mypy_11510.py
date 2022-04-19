def func1(cond: bool):
    if cond:
        def a(a: int, /) -> None:
            return None

        b: Callable[[int], None] = lambda a: None

    else:
        a: Callable[[int], None] = lambda a: None  # Mypy error: Name "a" already defined

        def b(a: int, /) -> None:
            return None

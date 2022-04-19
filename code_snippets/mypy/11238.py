def func(a: object, b: bool) -> None:
    if b:
        assert isinstance(a, int)
    else:
        assert isinstance(a, str)

    reveal_type(a)  # note: Revealed type is "builtins.object"

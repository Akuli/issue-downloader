def test() -> str:
    c = None
    for c in "":
        pass

    if c is None:
        return None

    return "foo"


print(test())

import typing


def test(l : typing.Sequence[str]) -> str:
    c = None
    for c in l:
        pass

    if c is None:
        return None

    return "foo"


print(test([]))
print(test(""))
print(test(["hello", "world"]))

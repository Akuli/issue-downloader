class Foo:
    def __init__(self) -> None:
        self.dirty = False


def test_source() -> None:
    foo = Foo()

    def bar() -> None:
        foo.dirty = True

    assert foo.dirty is False

    bar()

    assert foo.dirty is True
    print("unreachable?")

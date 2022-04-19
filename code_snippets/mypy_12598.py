class Foo:
    def foo(self) -> None:
        print("Foo!!!")

class Bar:
    def __init__(self) -> None:
        self.foo: Foo | None = Foo()

    def get_rid_of_foo(self) -> None:
        self.foo = None


bar = Bar()
if bar.foo is not None:
    bar.get_rid_of_foo()
    assert bar.foo is None
    print(1 + "lol")

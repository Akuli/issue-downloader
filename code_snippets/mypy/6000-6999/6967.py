from typing import Type
class Foo:
    def __init__(self, a):
        self.a = a

class Bar(Foo):
    def __init__(self):
        super().__init__("Bar")


def takes_foo(foo: Type[Foo]):
    x = foo("Foo")


takes_foo(Foo)
takes_foo(Bar)

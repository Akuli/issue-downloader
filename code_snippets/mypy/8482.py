from typing import Type

class Foo:
    def __init__(self):
        class Bar:
            pass

        self.Bar: Type[Bar] = Bar

foo = Foo()
bar: foo.Bar = foo.Bar()

reveal_type(foo.Bar)
reveal_type(bar)

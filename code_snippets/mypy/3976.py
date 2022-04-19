from typing import Type, Optional

class Foo:
    pass

def make_foo(cls: Optional[Type[Foo]] = None) -> Foo:
    x = Foo if cls is None else cls
    reveal_type(x)
    return x()

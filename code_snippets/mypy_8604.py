from typing import TypeVar

class Foo(object):
    pass

FooOrStr = TypeVar('FooOrStr', Foo, str)

def doit(reset: bool, arg: FooOrStr) -> FooOrStr:
    if reset:
        if isinstance(arg, Foo):
            reveal_type(arg)
            arg = Foo()
        elif isinstance(arg, str):
            reveal_type(arg)
            arg = ''
        else:
            raise TypeError()
    return arg

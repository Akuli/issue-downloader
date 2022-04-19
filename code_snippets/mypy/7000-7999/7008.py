from typing import *

class Foo:
    def __bool__(self) -> Literal[True]:
        return True

def some_foo() -> Foo:
    ...

def throw_error():
    raise Exception


if __name__ == '__main__':
    print(some_foo() or throw_error())
    #                   ^^^^^^^^^^^^^  impossible condition, unreachable

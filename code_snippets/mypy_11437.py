from typing import NoReturn

def foo() -> NoReturn:
    raise Exception

def bar() -> NoReturn:
    foo()
    foo()
    print("hi")  # no warning

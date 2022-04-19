from typing import overload, NoReturn


@overload
def f(a: str) -> int: ...
@overload
def f(a: str, b: NoReturn) -> NoReturn: ...

def f(a: str, b: NoReturn = ...) -> object: ...

    
b: bool
assert b

if not b:
    f("")  # error: Statement is unreachable ✅
    print("hi")

if not b:
    f("", b)  # error: Statement is unreachable ❌
    print("hi")


def f2(a: str, b: NoReturn) -> NoReturn: ...

if not b:
    f2("", b)  # no error ✅
    print("hi")

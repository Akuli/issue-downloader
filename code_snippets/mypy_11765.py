from typing import TypeGuard

def foo(value: TypeGuard[int]) -> None: ...  # no error

bar: TypeGuard[int] = True  # no error

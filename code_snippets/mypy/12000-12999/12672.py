from typing import overload

@overload
def f(a: int) -> int: ...
@overload
def f(a: str) -> str: ...

def f(a: int | str) -> bool | str: ...  # E: Overloaded function implementation cannot produce return type of signature 1

from typing import overload

@overload
def foo(a: int) -> None: ...

@overload
def foo(a: str) -> None: ...

def foo(a: object) -> None: ...

def bar(a: int) -> None: ...

foo(b=1)
bar(b=1)

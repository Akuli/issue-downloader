from typing import cast

def foo(a: object) -> None:
    cast(int, a)
    print(a + 1)

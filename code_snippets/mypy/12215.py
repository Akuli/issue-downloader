from typing import *

def foo() -> Iterable[Union[Tuple[Literal["foo"], int], Tuple[Literal["bar"], str]]]:
    for i in range(10):
        if i % 2 == 0:
            yield "foo", i
        else:
            yield "bar", str(i)

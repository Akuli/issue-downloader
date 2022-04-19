from typing import overload, Callable

@overload
def bar(fn: int) -> None:
    ...
@overload
def bar(fn: Callable[[int], object]) -> None:
    ...

def bar(fn: object) -> None:
    ...
    

bar(lambda value: reveal_type(value))
bar(lambda value: reveal_locals())

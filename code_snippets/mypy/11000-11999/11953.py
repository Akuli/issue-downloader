from typing import overload, Callable

@overload
def bar() -> None: ...
@overload
def bar(fn: Callable[[int], object]) -> None: ...

def bar(fn: object=1) -> None: ...
    

bar(lambda value: reveal_type(value))
bar(lambda value: reveal_locals())

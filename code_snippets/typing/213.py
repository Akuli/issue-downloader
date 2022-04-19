from typing import Iterable, Container

class IterableContainer(Iterable[int], Container[int]):
    ...

def f(x: IterableContainer) -> None: ...

class Test(IterableContainer):
    def __iter__(self): ...
    def __contains__(self, item: int) -> bool: ...

f(Test())

def assertIn(item: T, thing: Intersection[Iterable[T], Container[T]]) -> None:
    if item not in thing:
        # Debug output
        for it in thing:
            print(it)

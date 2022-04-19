# See http://stackoverflow.com/questions/3203286/how-to-create-a-read-only-class-property-in-python

from typing import *

T = TypeVar('T')
V = TypeVar('V')

class classproperty(Generic[T, V]):

    def __init__(self, getter: Callable[[Type[T]], V]) -> None:
        self.getter = getter

    def __get__(self, instance: Any, owner: Type[T]) -> V:
        # instance is really None, but we don't care
        return self.getter(owner)

class C:
    @classproperty    # <-- error here
    def foo(cls) -> int:
        return 42

reveal_type(C.foo)

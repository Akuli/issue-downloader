from typing import TypeVar, Generic

T = TypeVar("T")

class Foo(Generic[T]):
    def __init__(self): ...

class Bar(Generic[T]): ...

class FooChild(Foo[Bar[T]]):
    def __init__(self, blah: T):
        Foo.__init__(self)

from typing import TypeVar, Generic

T = TypeVar("T")

class Foo(Generic[T]):
    def __init__(self): ...

class Bar(Generic[T]): ...

class FooChild(Foo[T]): # Removed one level of nesting here
    def __init__(self, blah: T):
        Foo.__init__(self)

from typing import TypeVar, Generic

T = TypeVar("T")

class Foo(Generic[T]):
    def __init__(self): ...

class Bar(Generic[T]): ...

class FooChild(Foo[Bar[T]]):
    def __init__(self): # Removed the argument here
        Foo.__init__(self)

from typing import TypeVar, Generic

T = TypeVar("T")

class FooMetaclass(type, Generic[T]): pass

class Foo(metaclass=FooMetaclass[T]): # error: Dynamic metaclass not supported for "Foo"
    pass

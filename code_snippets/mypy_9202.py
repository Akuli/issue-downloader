import functools
from typing import Callable, cast, Generic, overload, Protocol, Type, TypeVar, Optional, TYPE_CHECKING, Union

T = TypeVar('T')
V = TypeVar('V')


# Arbitrary descriptor implementation.
class Property(Generic[T, V]):
    def __init__(self, fn: Callable[[T], V]):
        self.fn = fn

    @overload
    def __get__(self, obj: T, owner: Type[T]) -> V: ...

    @overload
    def __get__(self, obj: None, owner: Type[T]) -> Property[T, V]: ...    
     
         
    def __get__(self, obj: Optional[T], owner: Type[T]) -> Union[Property[T, V], V]:
        if obj is None:
            return self
        return self.fn(obj)



# Protocols that define pretty much the same thing.
class Proto1(Protocol):
    @property
    def prop1(self) -> int:
        ...

class Proto2(Protocol):
    prop1: int

class Proto3(Protocol):
    @functools.cached_property
    def prop1(self) -> int:
        ...

class Proto4(Protocol):
    @Property
    def prop1(self) -> int:
        ...        

# Implementation of each protocol above
class Foo1:
    @property
    def prop1(self) -> int:
        return 1

class Foo2:
    def __init__(self, x: int):
        self.prop1 = x
    
class Foo3:
    @functools.cached_property
    def prop1(self) -> int:
        return 3

class Foo4:
    @Property
    def prop1(self) -> int:
        return 4    


# All 4 statements below have RHS values that conform to the behavior
# defined by 'Proto1': objects that have a 'prop1' attribute that is an 'int',
# and that is not settable.
# No errors should be reported.
# It does not appear possible to define a common protocol that all 4 classes
# conform to, even though in code they all have valid common behavior:
# "intVal: int = x.prop1"

x : Proto1 = Foo1()
y : Proto1 = Foo2(2)
z : Proto1 = Foo3()
a : Proto1 = Foo4()

if TYPE_CHECKING:
    reveal_type(Foo1.prop1)
    reveal_type(Foo2.prop1)
    reveal_type(Foo3.prop1)
    reveal_type(Foo4.prop1)    


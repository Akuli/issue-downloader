from typing import TypeVar, Type, Callable, Union, Any

# t1 is a non-union type
t1: Type[bool] = bool
# t2 is a union type
t2: Union[Type[bool], Type[str]] = bool

# T1 is bound by a single Union type (supertype of bool and str)
T1 = TypeVar("T1", bound=Union[bool, str])
def foo1(t: Type[T1]) -> None: ...
foo1(t1)  # pass
foo1(t2)  # error: Value of type variable "T1" of "foo1" cannot be "object"

# T2 is bound by multiple types
T2 = TypeVar("T2", bool, str)
def foo2(t: Type[T2]) -> None: ...
foo2(t1)  # pass
foo2(t2)  # error: Value of type variable "T2" of "foo2" cannot be "object"
# note that this wouldn't work anyway as T2 cannot be Union[bool, str]

# T3 is not bound (can bind to object)
T3 = TypeVar("T3")
def foo3(t: Type[T3]) -> None: ...
foo3(t1)  # pass
foo3(t2)  # pass

# Shows that type deduction deduces Union when not using Type
# T1 = TypeVar("T1", bound=Union[bool, str])
def foo4(t: T1) -> None: ...
t3: bool = True
t4: Union[bool, str] = False
foo4(t3)  # pass
foo4(t4)  # pass

# Shows that type checking works when not using TypeVars, suggesting a problem
# with type deduction specifically
def foo5(t: Type[Union[bool, str]]) -> None: ...
foo5(t1)  # pass
foo5(t2)  # pass


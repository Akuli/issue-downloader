from typing import TypeVar, overload, Type, Tuple, Union

class Foo:
    pass

class Bar:
    pass

T1 = TypeVar('T1', bound=Foo)
T2 = TypeVar('T2', bound=Bar)

@overload
def f(cls: Type[T1]) -> Tuple[T1]:
    pass
@overload
def f(cls: Type[T2]) -> Tuple[T2]:
    pass

def f(cls: Union[
        Type[T1],
        Type[T2],
]) -> Union[
    Tuple[T1],
    Tuple[T2],
]:
    pass

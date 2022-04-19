from typing import Dict, Type
from typing_extensions import Protocol


class HasName(Protocol):
    name: str


class Class1(HasName):
    name = 'class1'

    def __init__(self, a: int):
        pass


class Class2(HasName):
    name = 'class2'

    def __init__(self, a: int, b: int):
        pass


class Class3(HasName):
    name = 'class3'

    def __init__(self, a: int):
        pass


# OK
def foo() -> Dict[Type[HasName], int]:
    d = {}
    for cls in (
        Class1,
        Class3,
    ):
        d[cls] = 1
    return d

# error: Incompatible return value type (got "Dict[ABCMeta, int]", expected "Dict[Type[HasName], int]")
def bar() -> Dict[Type[HasName], int]:
    d = {}
    for cls in (
        Class1,
        Class2,
        Class3,
    ):
        d[cls] = 1
    return d


# OK
def baz(a: int) -> Type[HasName]:
    if a == 1:
        return Class1
    elif a == 2:
        return Class2
    else:
        return Class3

from typing import Type


class Abstract:
    def __init__(self, one):
        pass


class A(Abstract):
    pass


class B(Abstract):
    def __init__(self, one, two):
        pass


MyClass: Type[Abstract]
if 2 + 2 > 4:
    MyClass = A
    more_kwargs = {}
else:
    MyClass = B
    more_kwargs = {"two": "two"}

# call-arg: Too many arguments for "Abstract"
my_class = MyClass("one", **more_kwargs)

#mypy(error): Unused "type: ignore" comment
my_class = MyClass("one", **more_kwargs)  # type: ignore

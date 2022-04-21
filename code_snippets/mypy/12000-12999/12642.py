from typing import List, Protocol, Type

class MyProto(Protocol):
    foo = List[str]

class MyClass:
    foo = ["bar"]

my_cls: Type[MyProto] = MyClass

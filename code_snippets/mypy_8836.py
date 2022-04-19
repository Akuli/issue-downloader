from typing import Type, Protocol

class MyProtocol(Protocol):
    name: str

class MyImplementation(MyProtocol):
    pass

foo: Type[MyProtocol] = MyImplementation

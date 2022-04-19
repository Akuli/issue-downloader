from typing import Protocol

class ProtocolInstance:
    def __call__(self) -> str: ...

class NotProtocolInstance:
    # equivalently, just remove __call__
    def __call__(self, value: int) -> int: ...

class SomeProtocol(Protocol):
    def __call__(self) -> str: ...

a: SomeProtocol = NotProtocolInstance  # false negative
b: SomeProtocol = NotProtocolInstance()  # what user meant to type, correctly errors

c: SomeProtocol = ProtocolInstance  # false negative
d: SomeProtocol = ProtocolInstance()  # no error

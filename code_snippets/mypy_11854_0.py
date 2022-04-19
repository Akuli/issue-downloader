from typing import TypeVar, Protocol

TValue = TypeVar('TValue', covariant=True)

# As an example, this does not give me any errors
class IValueProcessor(Protocol, Generic[TValue]):
    ...

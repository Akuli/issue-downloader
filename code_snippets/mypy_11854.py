from typing import TypeVar, Protocol

TValue = TypeVar('TValue', covariant=True)

# As an example, this does not give me any errors
class IValueProcessor(Protocol, Generic[TValue]):
    ...

from abc import ABC
from typing import Generic

from  .value import TValue

class Service(ABC, Generic[TValue]):  # Error occurs here, on `Generic`
    ...


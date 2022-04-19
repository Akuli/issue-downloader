from abc import ABC
from typing import Generic

from  .value import TValue

class Service(ABC, Generic[TValue]):  # Error occurs here, on `Generic`
    ...

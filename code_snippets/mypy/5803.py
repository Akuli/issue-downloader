from abc import ABC, abstractmethod
from typing import Any


class DataProperty:
    def __get__(self, instance: Any, owner: Any) -> str:
        return "X"


class BadBase1(ABC):
    @property
    @abstractmethod
    def id(self) -> str:
        raise NotImplementedError()


class BadBase2(ABC):
    id: str


class GoodBase(ABC):
    pass


class BadDerived1(BadBase1):
    id = DataProperty()   # Incompatible types in assignment (expression has type "DataProperty", base class "BadBase1" defined the type as "str")


class BadDerived2(BadBase2):
    id = DataProperty()   # Incompatible types in assignment (expression has type "DataProperty", base class "BadBase2" defined the type as "str")


class GoodDerived(GoodBase):
    id = DataProperty()


reveal_type(BadDerived1().id)  # Revealed type is 'Any'
reveal_type(BadDerived2().id)  # Revealed type is 'Any'
reveal_type(GoodDerived().id)  # Revealed type is 'builtins.str'

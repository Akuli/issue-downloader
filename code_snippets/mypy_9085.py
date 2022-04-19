from abc import ABC, abstractmethod
from typing import Type, Dict, List

class Abstract(ABC):
    @abstractmethod
    def method(self):
        pass

# this doesn't print an error, but should, because Abstract is not a concrete type
DICT: Dict[int, Type[Abstract]] = {0: Abstract}

# error as expected
DICT[1] = Abstract

# error as expected, lists are not affected
LIST: List[Type[Abstract]] = [Abstract];

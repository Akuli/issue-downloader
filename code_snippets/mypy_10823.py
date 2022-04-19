from collections.abc import Set
from dataclasses import dataclass

@dataclass(order=True)
class MySet(Set):
    pass

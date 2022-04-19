from typing import ClassVar, List, NamedTuple

class Employee(NamedTuple):
    """Represents an employee."""
    some_list_classvar: ClassVar[List] = []  # <- Doesn't work
    name: str
    id: int = 3

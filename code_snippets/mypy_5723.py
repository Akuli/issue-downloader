from dataclasses import dataclass, field
from mypy_extensions import TypedDict

class Person(TypedDict, total=False):
    name: str

@dataclass
class Job:
    person: Person = field(default_factory=Person)

from typing import NamedTuple
from dataclasses import make_dataclass, dataclass

Emp1 = NamedTuple('Emp1', [('name', str), ('id', int)])
r1 = Emp1('raymond', 'xyz')

Emp2 = make_dataclass('Emp2', [('name', str), ('id', int)])
r2 = Emp2('raymond', 'xyz')

class Emp3(NamedTuple):
    name: str
    id: int

r3 = Emp3('raymond', 'xyz')

@dataclass
class Emp4:
    name: str
    id: int

r4 = Emp4('raymond', 'xyz')

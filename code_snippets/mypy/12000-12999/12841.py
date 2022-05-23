from enum import Enum, verify, UNIQUE

@verify(UNIQUE)
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    CRIMSON = 1

from enum import Enum, nonmember

class Foo(Enum):
    BAR = 1
    BAZ = nonmember(2)

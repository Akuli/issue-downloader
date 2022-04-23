from enum import Enum, unique

@unique
class A(Enum):
   x = 1
   y = 1

def rand_int() -> int:
    ...

@unique 
class A(Enum):
    x = rand_int()
    y = rand_int()
    z = 0

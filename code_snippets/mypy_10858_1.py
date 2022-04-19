def rand_int() -> int:
    ...

@unique 
class A(Enum):
    x = rand_int()
    y = rand_int()
    z = 0

from enum import IntEnum

class MyIntEnum(IntEnum):
    A = 1
    B = 2

m: MyIntEnum

if m == 1:
    pass
else:
    reveal_type(m)

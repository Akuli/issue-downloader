from typing import Optional

a: Optional[int] = 1
b: Optional[int] = 1

if None not in (a, b):
    print(a + b)

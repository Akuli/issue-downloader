from typing import Optional

a: Optional[int] = 1
b: Optional[int] = 1

if None not in (a, b):
    print(a + b)

# mypy failed
if None not in (a, b):
    print(a + b)

# mypy passed
if a is not None and b is not None:
    print(a + b)


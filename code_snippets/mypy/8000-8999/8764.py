from typing import Union, Tuple

def func() -> Union[Tuple[None, None], Tuple[int, int]]:
    ...

a, b = func()

if a:
    print(a + b)

if a is not None:
    print(a + b)

# Unsupported operand types for + ("int" and "None")
# Right operand is of type "Optional[int]"

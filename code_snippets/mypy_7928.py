from typing import Optional

def my_func() -> bool:
  return True

created: bool = my_func()
a: Optional[int] = None
if created:
  a = 1
  z = a + 1 # This is OK

if created:
  x = a + 1 # Unsupported operand types for + ("None" and "int")

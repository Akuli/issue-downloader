from typing import Optional

def f(x:Optional[str]) -> bool:
  return bool(x) and g(x)

def f2(x:Optional[str]) -> bool:
  if x:
    return g(x)
  return False

def g(x: str) -> bool:
  return bool(x)

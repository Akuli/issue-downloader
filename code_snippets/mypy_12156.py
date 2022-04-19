import typing as t

T = t.TypeVar('T')
U = t.TypeVar('U')

def coalesce(a: T | None, b: U) -> t.Union[T, U]:
  if a is None:
    return b
  return a

def foo() -> int:
  return coalesce(42, None)

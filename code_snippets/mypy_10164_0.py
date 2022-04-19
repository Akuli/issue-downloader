import os
import typing as t
T = t.TypeVar('T')
R = t.TypeVar('R')

class flatmap(t.Generic[T, R]):

  def __init__(self, func: t.Callable[[T], R]) -> None:
    self.func = func

  def __ror__(self, value: t.Optional[T]) -> t.Optional[R]:
    if value is not None:
      return self.func(value)
    return None

# error: Cannot infer type argument 1 of "flatmap"
# error: "object" has no attribute "upper"
print(os.getenv('VARNAME') | flatmap(lambda m: m.upper()))
print(os.getenv('VARNAME') | flatmap(str.upper))  # ok

from typing import *

T_co = TypeVar('T_co', covariant=True)

class Col(Generic[T_co]):
  def __init__(self, items: Iterable[T_co]) -> None:
    self.items = items

  def any(self, pred: Callable[[T_co], bool]) -> bool:
    return any(map(pred, self.items))

  def any_zero(self, fn: Callable[[T_co], int]) -> bool:
    def pred(x: T_co) -> bool: # error: Cannot use type variable as a parameter
      return fn(x) == 0
    return self.any(pred)

class Unsafe(Generic[T_co]):
  def __init__(self, fn: Callable[[T_co], int]) -> None:
    self.fn = fn

  def get_fn(self) -> Callable[[T_co], int]:
    return self.fn

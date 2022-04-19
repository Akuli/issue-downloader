class Unsafe(Generic[T_co]):
  def __init__(self, fn: Callable[[T_co], int]) -> None:
    self.fn = fn

  def get_fn(self) -> Callable[[T_co], int]:
    return self.fn

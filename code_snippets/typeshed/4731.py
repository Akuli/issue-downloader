class A:

  @cached_property
  def f(self) -> int:  # f is `cached_property[int]`, f.__get__() -> int
    ...

  @property
  def g(self) -> int:  # f is `property[Any]`, g.__get__() -> Any
    ...

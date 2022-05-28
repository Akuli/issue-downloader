import typing
from typing import Type

T = typing.TypeVar("T")

del typing  # prevent accidental use below

class MySuper:
  @classmethod
  def f(cls: Type[T]) -> T:
    return cls()

class MySub(MySuper):
  @classmethod
  def f(cls: Type[T]) -> T:
    return super().f()

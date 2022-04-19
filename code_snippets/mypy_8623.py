from typing import cast, Any
from typing_extensions import Protocol, runtime_checkable
import typeguard

class Foo():

  @typeguard.typechecked
  def __init__(self, x: int, y: int,z: int = 3):
    self.x = x
    self.y = y
    self.z = z
    print("init")

f = Foo(9,10)
print(f)

func = type(f).__init__
print("__init__ func is {}".format(func))

if hasattr(func, '__wrapped__'):
  print("Path 1: is wrapped according to hasattr")
  print(cast(Any, type(f).__init__).__wrapped__)
else:
  print("Path 1: is not wrapped")


@runtime_checkable
class W(Protocol):
  __wrapped__: object

if isinstance(func, W):
  print("Path 2: is wrapped according to Protocol - mypy says this is unreachable")
  print(type(f).__init__.__wrapped__)
else:
  print("Path 2: is not wrapped")

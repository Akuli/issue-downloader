from typing import TypeVar


class Foo:
   pass


class Bar(Foo):
   pass

T = TypeVar('T', bound=Foo)

class Program:
  def get_foo_ish(self) -> T:
    ...

  @property
  def foo_ish(self) -> T:
    ...
    

program = Program()
bar1: Bar = program.get_foo_ish()
bar2: Bar = program.foo_ish  # error: Incompatible types in assignment (expression has type "T", variable has type "Bar")

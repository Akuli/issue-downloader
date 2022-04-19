class Foo(object):
  def __init__(self, x):
    self.x = x
  def __eq__(self, other):
    if not isinstance(other, Foo):
      return NotImplemented
    return self.x == other.x

set_of_foo = {Foo(1), Foo(2)}

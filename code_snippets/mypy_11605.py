import typing

class A:
  pass

class B:
  pass

T = typing.TypeVar("T", bound=A)
V = typing.TypeVar("V", bound=B)

_WhateverT = typing.TypeVar("_WhateverT", bound="Whatever[typing.Any]")
_WhateverPartTwoT = typing.TypeVar("_WhateverPartTwoT", bound="WhateverPartTwo[typing.Any]")

class Whatever(typing.Generic[T]):
  def something(self: _WhateverT) -> _WhateverT:
    return self
  def foo(self) -> T:
    pass

# here we specialize `Whatever` (only allow `A` to be passed in), and then generalize once again.
class WhateverPartTwo(Whatever[A], typing.Generic[V]):
  def something(self: _WhateverPartTwoT) -> _WhateverPartTwoT:
    return self
  def blah(self) -> V:
    pass

import typing

AT = typing.TypeVar("AT", bound="A")
BT = typing.TypeVar("BT", bound="B")

class A:
  def whatever(self: AT) -> AT: ...

class B:
  def whatever(self: BT) -> BT: ...
  

import typing

AT = typing.TypeVar("AT", bound="A")
BT = typing.TypeVar("BT", bound="B")

class A:
  def whatever(self: AT) -> AT: ...

class B:
  def whatever(self: BT) -> BT: ...
  
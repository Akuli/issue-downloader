
import typing as t

def spam(val: t.Union[t.Type, None] = None) -> None:

  def eggs(type_: t.Type) -> None:
    pass

  reveal_type(val)
  if isinstance(val, type):
    reveal_type(val)
    val, foo = None, val
    reveal_type(val)
    reveal_type(foo)
    return eggs(foo)

from typing import Any

@dataclass
class C:
  dict:object # This attribute name shadows `dict` type, but it should not shadow the name inside of the `class` lexical scope; that's not how python works.
  d:dict # This attribute is annotated as `dict`. The interpreter does not pick up the previous shadowed attribute, but mypy does.

c = C(dict={'a':1}, d={'b':2})
print(c.__annotations__)
assert c.__annotations__['d'] is dict # This proves that mypy is misunderstanding the name `dict`.

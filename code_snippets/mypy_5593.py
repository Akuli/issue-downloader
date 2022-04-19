from typing import Any, Type, TypeVar
from mypy_extensions import TypedDict

_T = TypeVar('_T')

class C(TypedDict):
  x: str

class D:
  x: str

def gen_row() -> Any:
  return {'x': 1}

def foo(cls: Type[_T]) -> _T:
  return gen_row()

def print_c(c: C):
  print(c)

def print_d(d: D):
  print(d)

print_c(foo(C))
print_d(foo(D))
reveal_type(foo(C))
reveal_type(foo(D))

[mypy]
ignore_missing_imports = True
strict_optional = True
warn_unused_ignores = True
warn_redundant_casts = True
warn_unused_configs = True
check_untyped_defs = True


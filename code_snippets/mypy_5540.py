from typing import Optional

def f(x:Optional[str]) -> bool:
  return bool(x) and g(x)

def f2(x:Optional[str]) -> bool:
  if x:
    return g(x)
  return False

def g(x: str) -> bool:
  return bool(x)

[mypy]
# This flag should be removed here and enabled per module when we have a
# considerable number of stubs for external libraries.
ignore_missing_imports = True
strict_optional = True
warn_unused_ignores = True
warn_redundant_casts = True
warn_unused_configs = True
check_untyped_defs = True


from typing import Union, Tuple, List

variable: List[Union[Tuple[int, int], Tuple[str, str]]] = []

element1 = variable[0]

print(element1[0] + element1[1])

[mypy]
python_version = 3.8
ignore_missing_imports = True
follow_imports = silent
show_column_numbers = True
disallow_untyped_calls = True
disallow_untyped_defs = True
disallow_incomplete_defs = True
check_untyped_defs = True
no_implicit_optional = True
warn_redundant_casts = True
warn_unused_ignores = True
warn_unreachable = True
strict_equality = True

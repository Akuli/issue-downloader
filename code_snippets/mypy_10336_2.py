[mypy]
python_version = 3.9
show_error_codes = True
pretty = True
files = moneyed

ignore_missing_imports = False
no_implicit_optional = True
strict_equality = True
strict_optional = True
check_untyped_defs = True
disallow_incomplete_defs = True
disallow_untyped_defs = True
disallow_untyped_calls = True
disallow_untyped_decorators = True
disallow_subclassing_any = True

warn_unused_configs = True
warn_redundant_casts = True
warn_unused_ignores = True
warn_return_any = True
warn_unreachable = True

[mypy]
ignore_missing_imports = True
disallow_untyped_defs = True
disallow_incomplete_defs = True
no_implicit_optional = True
warn_redundant_casts = True
warn_return_any = True
warn_unreachable = True
local_partial_types = True
no_implicit_reexport = True
strict_equality = True
show_error_codes = True
show_traceback = True
pretty = True
plugins = pydantic.mypy
# Various "exclude" options (see above)
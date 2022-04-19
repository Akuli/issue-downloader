[mypy]
plugins = sqlmypy
disallow_untyped_calls = False
disallow_untyped_defs = True
ignore_missing_imports = True
warn_return_any = False
follow_imports = silent
allow_redefinition = True

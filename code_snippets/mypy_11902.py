[mypy]
plugins = sqlalchemy.ext.mypy.plugin, pydantic.mypy
ignore_missing_imports = True
disallow_untyped_defs = True

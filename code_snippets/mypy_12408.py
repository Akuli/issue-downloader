[mypy]
follow_imports = silent
ignore_missing_imports = True
check_untyped_defs = True
disallow_untyped_defs = True
no_implicit_optional = True
strict_equality = True
warn_redundant_casts = True
python_version = 3.8
platform = linux
plugins = pydantic.mypy
namespace_packages = True

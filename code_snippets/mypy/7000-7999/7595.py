class X:
    def __new__(cls) -> "X":
        return super(type, cls).__new__(cls)    # error: Argument 2 for "super" not an instance of argument 1

[mypy]
python_version=3.6
incremental=True
ignore_missing_imports=True
follow_imports=normal
warn_redundant_casts=True
warn_unused_ignores=True
strict_optional=True
no_implicit_optional=True
disallow_untyped_defs=True
disallow_any_generics=True


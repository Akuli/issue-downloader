from typing_extensions import final


class Base:
    @final
    def __init__(self):
        pass


class A(Base):
    def __init__(self):  # no error raised
        pass


class B(Base):
    def __init__(self) -> None:  # raises an error
        pass

[mypy]
ignore_missing_imports = True
strict_optional = True
no_implicit_optional = True
check_untyped_defs = True
disallow_incomplete_defs = True
disallow_any_unimported = True
disallow_untyped_decorators = True


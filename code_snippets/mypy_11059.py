def foo(): pass  # type: ignore
foo()  # type: ignore[no-untyped-call]

[mypy]
strict = True
disable_error_code = no-untyped-call

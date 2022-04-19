[mypy]
python_version = 3.8

disallow_any_expr = False
disallow_any_decorated = False
disallow_any_explicit = True
disallow_any_generics = True
disallow_subclassing_any = True

disallow_untyped_calls = True
disallow_untyped_defs = True
check_untyped_defs = False
disallow_untyped_decorators = False

no_implicit_optional = True

warn_redundant_casts = True
warn_unused_ignores = True
warn_return_any = True
warn_unreachable = True
strict_equality = True

allow_redefinition = False

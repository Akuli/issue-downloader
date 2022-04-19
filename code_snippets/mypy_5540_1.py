[mypy]
# This flag should be removed here and enabled per module when we have a
# considerable number of stubs for external libraries.
ignore_missing_imports = True
strict_optional = True
warn_unused_ignores = True
warn_redundant_casts = True
warn_unused_configs = True
check_untyped_defs = True

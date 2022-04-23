from datetime import date, datetime

if datetime.now() < date.today():
    print("that's a surprise!")

python_version=3.8
incremental=True
follow_imports=normal
warn_redundant_casts=True
warn_unused_ignores=True
strict_optional=True
strict_equality=True
no_implicit_optional=True
disallow_untyped_defs=True
disallow_any_generics=True

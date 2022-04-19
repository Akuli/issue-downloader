import typing as t

def get_print_fn(quiet: bool) -> t.Callable[..., None]:
    """Return the standard print function if quiet is False, else an empty function."""
    return (lambda *args, **kwargs: None) if quiet else print

import typing as t

def get_print_fn(quiet: bool) -> t.Callable[..., None]:
    """Return the standard print function if quiet is False, else an empty function."""
    return print if not quiet else lambda *args, **kwargs: None

[mypy]
python_version = 3.7
warn_return_any = True
warn_unused_ignores = True
warn_unreachable = True
namespace_packages = True
show_column_numbers = True
strict_equality = True
no_implicit_optional = True
disallow_untyped_defs = True
disallow_any_generics = True
disallow_untyped_calls = True

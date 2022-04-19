from typing import type_check_only, ParamSpec, Concatenate, Callable

@type_check_only  # no warning about unsupported functionality
def foo() -> None: ...

P = ParamSpec("P")
def bar(func:  # error: The first argument to Callable must be a list of types or "..."
    Callable[
      Concatenate[P, int],
      None,
    ]
) -> None:  # 
    ...

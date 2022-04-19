import typing as t

def get_print_fn(quiet: bool) -> t.Callable[..., None]:
    """Return the standard print function if quiet is False, else an empty function."""
    return print if not quiet else lambda *args, **kwargs: None

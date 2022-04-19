import typing as t

def get_print_fn(quiet: bool) -> t.Callable[..., None]:
    """Return the standard print function if quiet is False, else an empty function."""
    return (lambda *args, **kwargs: None) if quiet else print

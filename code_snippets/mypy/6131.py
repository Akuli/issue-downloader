EnvironDict = TypedDict("EnvironDict", {
    "wsgi.version": Tuple[int, int],
    "wsgi.input": IO[str],
# ...
}, default_type=str, total=False)

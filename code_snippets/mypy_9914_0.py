class ProgressLogger(NamedTuple):
    progress: Callable[[T], T]

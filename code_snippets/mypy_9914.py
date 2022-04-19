class ProgressLogger(NamedTuple):
    progress: Callable[[T], T]

def bar(progress_logger: ProgressLogger) -> None:
    pass


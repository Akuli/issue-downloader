def get_index(l: list, i: int) -> Any | NoResult:  # this kind of NoResult means that we don't know the actual error, shortcut for NoResult[Exception]
    # with type: unwrap instruction Mypy will not complain about this line
    return l[i]  # type: unwrap

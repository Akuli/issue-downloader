class _reader(Iterator[List[str]]):
    dialect: Dialect
    line_num: int
    if sys.version_info >= (3, 0):
        def __next__(self) -> List[str]: ...
    else:
        def next(self) -> List[str]: ...

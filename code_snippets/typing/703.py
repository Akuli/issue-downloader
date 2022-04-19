def assert_positive(x: object) -> AssertsInstance["x", int]:
    assert isinstance(x, int) and x > 0


def is_positive(x: object) -> ChecksInstance["x", int]:
    return isinstance(x, int) and x > 0

def my_func(x: Union[int, str]) -> None:
    if is_positive(x):
        # x must be an int
        ...
    else:
        # x can be an int or str
        ...

from typing import Union, NoReturn, overload

@overload
def assert_int(x: int) -> None: ...
@overload
def assert_int(x: str) -> NoReturn: ...

def assert_int(x):
    assert isinstance(x, int)

y: Union[int, str]
assert_int(y)
reveal_type(y)  # should be: int; currently Union[int, str]

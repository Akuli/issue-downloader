from typing import NoReturn

def assert_never(x: NoReturn) -> NoReturn:
    raise AssertionError(f"Invalid value: {x!r}")

from typing import Union

def type_checking_ok(foo: Union[str, int]) -> None:
    if isinstance(foo, str):
        print("str")
    elif isinstance(foo, int):
        print("int")
    else:
        assert_never(foo)

def type_checking_ko(foo: Union[str, int]) -> None:
    if isinstance(foo, str):
        print("str")
    else:
        assert_never(foo)

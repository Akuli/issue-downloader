@singledispatch
def foo(data: object) -> NoReturn:
    raise ValueError(f"Unhandled type {type(data)}")
@foo.register
def _(data: str) -> str:
    return data
@foo.register
def _(data: int) -> str:
    return str(data)

a = foo(7)
reveal_type(a)

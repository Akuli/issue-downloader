def my_open(name: str, write: bool):
    with open(name, 'wb' if write else 'rb') as f:
        content = f.read()

if typing.STRICTER_STUBS:
    AnyOrUnion = typing.Union
else:
    AnyOrUnion = typing.Any

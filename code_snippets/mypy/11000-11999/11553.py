class MyDict(TypedDict, total=False):
    a: int
    b: str
    ...

MyDictKeys = Union[Literal['a'], Literal['b']]

def is_mydict_key(key: str) -> TypeGuard[WidgetOptionKeys]:
    return key in MyDictKeys.__annotations__

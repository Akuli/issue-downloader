MyDict = TypedDict('MyDict', {'foo': int, 'bar': bool})
def fn() -> MyDict:
    pass

def fn() -> TypedDict({'foo': int, 'bar': bool}):
    pass

def fn() -> TypedDict(foo=int, bar=bool):
    pass

MyType = TypedDict({
    'foo': int,
    'bar': TypedDict({
        'baz': int,
    })
})

async def get_from(foo: Foo[T]) -> T:
    return foo.contents

async def foo() -> Iterable[int]:               
    async def bar(i: int) -> int:
        return i  
    
    xs = [1, 2, 3]
    
    return (await bar(x) for x in xs)

async def foo_errors() -> Iterable[int]:
    async def bar(i: int) -> int:
        return i

    xs = [1, 2, 3]
    
    for x in xs:
        v = await bar(x)
        yield v

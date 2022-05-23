def nothing() -> None:
    ...

def foo() -> None:
    x = nothing()  # E: "nothing" does not return a value

async def async_nothing() -> None:
    ...

async def async_foo() -> None:
    x = await async_nothing()

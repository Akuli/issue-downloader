def some_deferred() -> Awaitable[int]: ...
def some_future() -> Awaitable[int]: ...

async def x() -> Awaitable[List[int]]:
    y = []
    y.append(await some_deferred())
    y.append(await some_future())
    return y

def some_deferred() -> Awaitable[int, Deferred]: ...
def some_future() -> Awaitable[int]: ... # presumably Future is the default

async def x() -> Awaitable[List[int]]:
    y = []
    y.append(await some_deferred()) # <-- automatically specialize to `Awaitable[List[int], Deferred]` here, if possible?
    y.append(await some_future()) # <-- type error!
    return y

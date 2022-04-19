from asyncio import gather


async def returns_dict() -> dict:
    return {}


async def returns_int() -> int:
    return 1


async def test():
    reveal_type(await gather(returns_dict(), returns_int()))

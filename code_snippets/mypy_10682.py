from asyncio import gather


async def returns_dict() -> dict:
    return {}


async def returns_int() -> int:
    return 1


async def test():
    tasks = (returns_dict(), returns_int())
    reveal_type(await gather(*tasks))  # note: Revealed type is "Any"

from asyncio import gather


async def returns_dict() -> dict:
    return {}


async def returns_int() -> int:
    return 1


async def test():
    reveal_type(await gather(returns_dict(), returns_int()))

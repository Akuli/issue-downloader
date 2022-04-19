import asyncio
from typing import Type, TypeVar
import aiohttp

ResponseType = TypeVar("ResponseType", str, bytes)
# ResponseType = TypeVar("ResponseType")  <- This works, but it's not what I need in real life

async def post(response_type: Type[ResponseType]) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get("https://google.com") as res:
            res.raise_for_status()

asyncio.run(post(str))

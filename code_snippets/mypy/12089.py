reveal_type(asyncio.gather(*[asyncio.sleep(1), asyncio.sleep(1)]))

reveal_type(asyncio.gather(*[reveal_type(asyncio.sleep(1)), asyncio.sleep(1)]))

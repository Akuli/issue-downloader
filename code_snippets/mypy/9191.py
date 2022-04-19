def ret_nothing() -> None:
    pass


def use_nothing() -> None:
    ret = ret_nothing()


async def async_ret_nothing() -> None:
    pass


async def async_use_nothing() -> None:
    ret = await async_ret_nothing()


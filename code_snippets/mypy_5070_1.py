class BaseClass:
    async def gen1(self) -> AsyncGenerator[str, None]:
        pass
reveal_type(BaseClass.gen1)

class MyClass(BaseClass):
    async def gen1(self) -> AsyncGenerator[str, None]:
        yield 'tick'
reveal_type(MyClass.gen1)

from typing import Literal

LiteralStrHello = Literal["hello"]
LiteralStrWorld = Literal["world"]


class A:
    def __getattr__(self, name: LiteralStrHello) -> LiteralStrWorld:
        assert name == "hello"
        return "world"

    def __getattribute__(self, name: LiteralStrHello) -> LiteralStrWorld:
        assert name == "hello"
        return "world"

from typing import ByteString

x: ByteString = b""

def foo(y: bytes) -> None:
    pass

foo(x)

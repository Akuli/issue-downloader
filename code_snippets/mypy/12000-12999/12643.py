from typing import Union

Buffer = Union[bytes, bytearray, memoryview]

def f(data: Buffer) -> str:
    if not isinstance(data, bytes):
        data = bytes(data)

    return data.decode()

[tool.mypy]
warn_unused_ignores = true
show_error_codes = true
strict = true

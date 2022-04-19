from typing import overload

class Snafu(object):
    @overload
    @staticmethod
    def snafu(value: None) -> None: ...

    @overload
    @staticmethod
    def snafu(value: bytes) -> bytes: ...

    @overload
    @staticmethod
    def snafu(value: str) -> bytes: ...

    @staticmethod
    def snafu(value):
        return bytes(value, encoding='UTF-16')

print(Snafu().snafu('123'))

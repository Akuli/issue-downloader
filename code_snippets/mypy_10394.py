import typing

NoneType = type(None)

class NullableString:
    @typing.overload
    def __new__(cls: type, arg: None) -> 'NoneType':
        pass
    @typing.overload
    def __new__(cls: type, arg: str) -> 'NullableString':
        pass
    def __new__(cls: type, arg: typing.Optional[str]):
        if arg is None:
            return NoneType.__new__(type(None))
        elif isinstance(arg, str):
            return str.__new__(cls)

NullableString(None)

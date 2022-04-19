import typing

@typing.overload
def get_param(param: typing.Literal['some_float']) -> float: ...


@typing.overload
def get_param(param: typing.Literal['some_other_int']) -> int: ...


@typing.overload
def get_param(param: typing.Literal['further_str']) -> str: ...


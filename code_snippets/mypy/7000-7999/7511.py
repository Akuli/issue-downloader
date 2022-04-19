import typing


def no_return_optional(arg) -> typing.Optional[str]:
    if arg:
        return "false"


def no_return(arg) -> str:
    if arg:
        return "false"


a1 = no_return_optional(True)
a2 = no_return_optional(False)
reveal_type(a1)
reveal_type(a2)

b1 = no_return(True)
b2 = no_return(False)
reveal_type(b1)
reveal_type(b2)

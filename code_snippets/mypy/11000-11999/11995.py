from typing import Union, NewType

Int = NewType("Int", int)
Float = NewType("Float", float)

def raw_types(arg: Union[int, float, None]) -> None:
    if isinstance(arg, int):
        reveal_type(arg)  # Revealed type is "builtins.int"
    elif isinstance(arg, float):
        reveal_type(arg)  # Revealed type is "builtins.float"
    else:
        reveal_type(arg)  # Revealed type is "None"

def new_types(arg: Union[Int, Float, None]) -> None:
    if isinstance(arg, int):
        reveal_type(arg)  # Revealed type is "__main__.Int"
    elif isinstance(arg, float):
        reveal_type(arg)  # Revealed type is "Union[__main__.Int, __main__.Float]" (NARROWING FAILED)
    else:
        reveal_type(arg)  # Revealed type is "None"

def new_types_not_optional(arg: Union[Int, Float]) -> None:
    if isinstance(arg, int):
        reveal_type(arg)  # Revealed type is "__main__.Int"
    elif isinstance(arg, float):
        reveal_type(arg)  # Revealed type is "__main__.Float"
    else:
        reveal_type(arg)

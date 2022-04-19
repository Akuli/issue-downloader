from typing import Optional, Final

def example_func(value: Optional[int] = None):

    condition: Final = value is not None

    if condition: 
        reveal_type(value)  # Revealed type is "Union[builtins.int, None]"
        value = value + 1   # MYPY ERROR

    if value is not None:
        reveal_type(value)  # Revealed type is "builtins.int"
        value = value + 1   # MYPY OK
    return 0

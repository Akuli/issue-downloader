x: Union[int, str]

if isinstance(x, str):
    reveal_type(x)  # Revealed type is 'builtins.str'
    x = x + 1   # E: Unsupported operand types for + ("str" and "int")
    reveal_type(x)  # Revealed type is 'builtins.int'  - CHANGED

if isinstance(x, int):
    reveal_type(x)  # Revealed type is 'builtins.int'
    x = x + 'a'   # E: Unsupported operand types for + ("str" and "int")
    reveal_type(x)  # Revealed type is 'builtins.int'  - DIDN'T CHANGE

x: Union[int, str] = 'a'
x = x + 1 # error
reveal_type(x)  # Revealed type: int


from typing import Union
x = 0  # type: Union[int, str]
reveal_type(x)  # Revealed type is 'Union[builtins.int, builtins.str]'
x = 0
reveal_type(x)  # Revealed type is 'builtins.int'

x = "foo" # type: Optional[str]
x + "bar"  # E: Unsupported operand types for + ("Union[str, None]" and "str")


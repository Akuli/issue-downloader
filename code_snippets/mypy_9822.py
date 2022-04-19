from typing import Union

foo: Union[str, bytes]  
"zoo" in foo  # no error
"zoo" + foo  # err: Unsupported operand types for + ("str" and "bytes")

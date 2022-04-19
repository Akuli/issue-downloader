from typing import NoReturn

# Incompatible types in assignment (expression has type "object", variable has type "Type[NoReturn]")  [assignment]
foo: type[NoReturn] = NoReturn 

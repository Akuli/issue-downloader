from typing import Any, AnyStr
def foo(arg1: AnyStr, arg2: AnyStr) -> None: ...
bar: Any = ""
foo(1, "") # Error correctly reported
foo(b"", bar) # No error (correct)
foo(1, bar) # No error (false negative)

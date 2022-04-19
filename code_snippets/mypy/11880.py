from typing import Any, TypeVar, Union

T = TypeVar("T")
V = TypeVar("V", str, bytes)

def check_t(x: T | list[T]) -> T: ...
def check_v(x: V | list[V]) -> V: ...

x_str: str
x_list_any: list[Any]
x_str_list_any: str | list[Any]

# mypy does the correct thing here

reveal_type(check_t(x_str))  # str
reveal_type(check_t(x_list_any))  # list[Any] | Any
reveal_type(check_t(x_str_list_any))  # str | list[Any] | Any
reveal_type(check_v(x_str))  # str

# but maybe not here

# E: Value of type variable "V" of "check_v" cannot be "Union[List[Any], Any]"
# N: Revealed type is "Union[builtins.list[Any], Any]"
reveal_type(check_v(x_list_any))
# E: Value of type variable "V" of "check_v" cannot be "Union[str, List[Any], Any]"
# N: Revealed type is "Union[builtins.str, builtins.list[Any], Any]"
reveal_type(check_v(x_str_list_any))

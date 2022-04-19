import functools
from typing import TypeVar

_T = TypeVar("_T")


def my_func(elem: _T) -> list[_T]:
    return [elem]
    
my_func_cached = functools.lru_cache(my_func)

a = my_func("a")
reveal_type(a)  # Revealed type is "builtins.list[builtins.str*]"
a_c = my_func_cached("a")

# ERROR: this should be "builtins.list*[builtins.str]"
reveal_type(a_c)  # Revealed type is "builtins.list*[_T`-1]"


# this works

def my_func_str(elem: str) -> list[str]:
    return [elem]
    
my_func_str_cached = functools.lru_cache(my_func_str)

a_str = my_func_str("a")
reveal_type(a_str)  # Revealed type is "builtins.list[builtins.str]"
a_str_c = my_func_str_cached("a")
reveal_type(a_str_c)  # Revealed type is "builtins.list*[builtins.str]"

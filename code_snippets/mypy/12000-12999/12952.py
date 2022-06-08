from __future__ import annotations

from typing import TypeAlias, TypeVar, get_args, TypeGuard

A: TypeAlias = int | float
d = (int,float)

#T = TypeVar("T", int, float) # Correctly working if uncommented

T = TypeVar("T", *d) 
#T = TypeVar("T", *get_args(A)) # Same results using this tuple of types instead of d

def is_valid(value:A, t:type[T])->TypeGuard[T]:
    return isinstance(A, t)

def is_int(value:A) -> TypeGuard[int]:
    return is_valid(value, int)

def is_float(value:A) -> TypeGuard[float]:
    return is_valid(value, float)

def is_str(value:A) -> TypeGuard[str]: 
    return is_valid(value, str) # Should give error if T follows the type constraints

a: A = 34
reveal_type(a) # Union[builtins.int, builtins.float]
if is_valid(x:= a, int):
    reveal_type(x)  # Should give builtins.int instead gives type is "T?"
    
if is_int(x:=a):
    reveal_type(x) # Gives type is "builtins.int" in both cases

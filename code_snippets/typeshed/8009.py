from typing import TypeVar, TypeGuard

T = TypeVar('T')

def iscoroutinefunction(func: T) -> TypeGuard[T]: ...

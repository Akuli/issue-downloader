from typing import Callable

def bar(x):  return 5

foo : Callable[[float],int] = bar

foo("test")

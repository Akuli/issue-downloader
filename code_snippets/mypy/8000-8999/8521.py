from typing import Callable

def bar(x):  return 5

foo : Callable[[float],int]
foo = bar

foo("test")

from typing import Callable

def bar(x):  return 5

foo : Callable[[float],int] = bar

foo("test")

from typing import Tuple

foo : Tuple[str,int]
foo = (1,3)


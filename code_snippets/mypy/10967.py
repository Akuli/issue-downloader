import types
from typing import List

from .my_module import *

__all__ = []
submodules: List[types.ModuleType] = [my_module]
for submodule in submodules:
    __all__.extend(submodule.__all__)

__all__ = ["my_var"]

my_var = "hello!"

from my_app import my_module

print(my_module.my_var)

from my_app.my_pkg import my_module

from my_app import my_pkg

print(my_pkg.my_var)


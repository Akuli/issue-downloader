import types
from typing import List

from .my_module import *

__all__ = []
submodules: List[types.ModuleType] = [my_module]
for submodule in submodules:
    __all__.extend(submodule.__all__)

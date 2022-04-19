# b.py

from a import *

x: str  # Name "x" already defined (possibly by an import)
reveal_type(x)  # Revealed type is "builtins.int"

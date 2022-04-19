# main.py
import a
reveal_type(a.b)

# file a/__init__.py
from a.c import C

# file a/b.py
class B: ...

# file a/c.py
from a.b import B
class C: ...

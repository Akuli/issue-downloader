# test.py

import sys

assert sys.platform == "win32"

class Foo:
    pass

foo = Foo()
foo.bar = 1  # type: ignore[attr-defined]

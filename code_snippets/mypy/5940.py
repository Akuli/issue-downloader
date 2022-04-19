import sys

if sys.version_info < (3,):
    class X:
        def foo(self) -> int: ...
    class Y(X):
        def foo(self) -> str: ...  # type: ignore

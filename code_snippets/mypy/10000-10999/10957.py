#!/usr/bin/env python3

import sys

# test.py:9: error: Variable annotation syntax is only supported in Python 3.6 and greater
def f() -> None:
        if sys.version_info <= (3,6):
                raise RuntimeError('python 3.6 or greater required')
        x: int = 0
        print(x)


# No mypy error
def g() -> None:
        if sys.version_info <= (3,6):
                raise RuntimeError('python 3.6 or greater required')
        else:
                x: int = 0
                print(x)

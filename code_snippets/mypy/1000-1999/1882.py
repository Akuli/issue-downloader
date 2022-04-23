import six

if six.PY2:
    n = 42

def main():
    # type: () -> None
    if six.PY3:
        print("n is only defined on python 2.")
    else:
        print("n =", n)
        # ... some number crunching on n

import six

if six.PY2:
    n = 42

def main():
    # type: () -> None
    if six.PY3:
        print("n is only defined on python 2.")
        return
    print("n =", n)
    # ... some number crunching on n

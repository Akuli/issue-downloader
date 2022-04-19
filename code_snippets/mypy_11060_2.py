# ok for Python but error for mypy: Name "x" already defined
x = 0
[x := x + y for y in range(2)]

# ok for mypy, but Python error: NameError: name 'z' is not defined
[z := z + y for y in range(2)]


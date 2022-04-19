# mypy failed
if None not in (a, b):
    print(a + b)

# mypy passed
if a is not None and b is not None:
    print(a + b)

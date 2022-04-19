def f(): pass

y = 1
if f():
    y = None  # None not compatible with int
reveal_type(y)

if f():
    z = 1
else:
    z = None  # None not compatible with int
reveal_type(z)

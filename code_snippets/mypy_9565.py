class A: ...
class B(A):
    x: int
class C(A):
    x: int

o: object
assert isinstance(o, (B, C))
_ = o.x

if isinstance(o, B):
    ...
elif isinstance(o, C):
    ...
else:
    raise AssertionError("unreachable")

_ = o.x

o: object
assert isinstance(o, (B, C))

o: Union[B, C]

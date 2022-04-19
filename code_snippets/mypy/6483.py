from mypy_extensions import TypedDict

class FooBase(TypedDict):
    x: int  # a required field

class Foo(FooBase, total=False):
    y: int  # an optional field

f = Foo(x=5)

# current situation
f['x']  # ok
f['y']  # ok
f.get('y', 0)  # ok

# "strict" situation
f['x']  # ok (item is always present)
f['y']  # FAIL
f.get('y', 0)  # ok (explicit fallback is needed)

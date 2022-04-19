from types import NoneType

def foo(a: NoneType):  # sus alert, NoneType is a mess in the type realm, you should use `None` or `type[None]` instead.
    print(isinstance(a, NoneType))

class A:
    pass

class B(A):
    foo: str

def bar(a: A):
    assert isinstance(a, B)
    return a.foo

class A:
    @property
    def foo(self):
        return 'a'

A.foo.fget(A())

class A(object):
    def do(self):
        from package import do_b      # this gives an error
        # from package.b import do_b  # this works
        return do_b(self)

from package.a import A

def do_b(a):
    # type: (A) -> str
    return 'foo'

from .b import do_b

from package.a import A

a = A()
print(a.do())

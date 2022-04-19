class Base:
    def foo(self): pass

class Mix: pass

class A(Mix, Base): pass

class B(Mix, Base): pass

def foo() -> None:
    a = A() if bool() else B()
    reveal_type(a)  # Shows Mix
    a.foo()  # E: "Mix" has no attribute "foo"

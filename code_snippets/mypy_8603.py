class A():
    pass

class B():
    def __init__(self):
        self.a = A

b = B()

class C(b.a):
    pass

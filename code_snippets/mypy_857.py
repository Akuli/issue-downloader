class A:
    def __init__(self, a): pass
class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        self._inner = super(B, self)

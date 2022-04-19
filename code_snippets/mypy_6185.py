
class A():
    @property
    def a(self) -> float:
        return 0.5

class B():
    @property
    def a(self) -> float:
        return 1.5

class C(A, B):
    is_a:bool = True
    @property
    def a(self) -> float:
        if self.is_a:
            return A.a.fget(self)
        else:
            return B.a.fget(self)


if __name__ == '__main__':
    c = C()
    assert c.a ==0.5
    c.is_a = False
    assert c.a == 1.5

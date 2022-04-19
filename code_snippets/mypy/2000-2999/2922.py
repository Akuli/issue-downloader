class A(metaclass=abc.ABCMeta): pass
class B: pass
A.register(B)
a: A = B()  # currently E: Incompatible types in assignment (expression has type "B", variable has type "A")
print(isinstance(a, A))  # -> True

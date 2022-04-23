class A:
    def __add__(self, other) -> int:
        ...
    def __iadd__(self, other) -> 'A':
        ...

class C(A):
    #  error: Return type of "__iadd__" incompatible with "__add__" of supertype "A"
    def __iadd__(self, other) -> 'C':
        ...

__add__
__iadd__
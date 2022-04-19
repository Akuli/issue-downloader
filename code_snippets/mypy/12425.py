class A:
    pass

B = type(A)('B', (A,), {})
b = B()

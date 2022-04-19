from types import new_class

X = new_class('X', (int,))

def sum_two(a: X, b: X) -> X:
    return a + b

print(sum_two(X(2), X(3)))

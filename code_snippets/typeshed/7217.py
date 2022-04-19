from numbers import Real

def test(f: Real) -> Real:
    return f

test(1.32)
# error: Argument 1 to "test" has incompatible type "float"; expected "Real"

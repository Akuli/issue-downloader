pow(complex(1), 2, 2)  # no type error?
pow(float(1), 2, 2)  # still no type error?

from numbers import Complex
my_complex: Complex = complex(1)  # type: ignore [assignment]  # see 3186
pow(my_complex, 2, 2)  # No overload variant of "pow" matches argument types "Complex", "int", "int"

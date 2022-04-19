import sys
if sys.version_info >= (3, 8):
    from math import comb
else:
    def comb(n: int, k: int) -> int:  # All conditional function variants must have identical signatures
        return int(factorial(n) / factorial(k) / factorial(n - k))

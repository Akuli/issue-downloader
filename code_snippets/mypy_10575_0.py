try:
    from math import comb
except ImportError:
    def comb(n: int, k: int) -> int:  # All conditional function variants must have identical signatures
        return int(factorial(n) / factorial(k) / factorial(n - k))

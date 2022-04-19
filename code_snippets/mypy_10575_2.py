try:
    from math import comb
except ImportError:
    def comb(__n: int, __k: int) -> int:  # <no more warning>
        return int(factorial(__n) / factorial(__k) / factorial(__n - __k))

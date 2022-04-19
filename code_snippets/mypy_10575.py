try:
    from math import comb
except ImportError:
    def comb(n: int, k: int) -> int:  # All conditional function variants must have identical signatures
        return int(factorial(n) / factorial(k) / factorial(n - k))

import sys
if sys.version_info >= (3, 8):
    from math import comb
else:
    def comb(n: int, k: int) -> int:  # All conditional function variants must have identical signatures
        return int(factorial(n) / factorial(k) / factorial(n - k))

try:
    from math import comb
except ImportError:
    def comb(__n: int, __k: int) -> int:  # <no more warning>
        return int(factorial(__n) / factorial(__k) / factorial(__n - __k))


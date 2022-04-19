from typing import SupportsFloat

class Floaty:
    def __float__(self): ...

class Supporter(SupportsFloat):
    def __float__(self): ...

reveal_type(Floaty() if bool() else 0)
reveal_type(Supporter() if bool() else 0)

# foo.py
from typing import Tuple, Type

class A: pass
class B: pass

PlainBases = (A, B)
reveal_type(PlainBases)
# ^ Revealed type is 'Tuple[def () -> foo.A, def () -> foo.B]'

class PlainC(*PlainBases):
# ^ Invalid base class
    pass

AnotatedBases = (A, B)  # type: Tuple[Type[A], Type[B]]
reveal_type(AnotatedBases)
# ^ Revealed type is 'Tuple[Type[foo.A], Type[foo.B]]'

class AnotatedC(*AnotatedBases):
# ^ Invalid base class
    pass

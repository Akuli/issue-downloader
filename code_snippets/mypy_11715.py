from enum import Enum

class E(Enum):
    _order_ = 'X Y Z'  # Should be 'X Y'
    X = 1
    Y = 2

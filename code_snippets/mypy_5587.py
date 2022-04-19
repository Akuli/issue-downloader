from typing import ClassVar
  
class C:
    x: ClassVar = 1

reveal_type(C.x)  # Revealed type is 'Any'

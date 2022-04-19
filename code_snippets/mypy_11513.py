from b import B
from a import b

main = B()

from b import b as b
from main import main

reveal_type(main)

b = 1

class B:
    ...


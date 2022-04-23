x = 123

from m1 import x
__all__ = []

from m2 import x
__all__ = ['x']

x: int



from m2 import x as x

from m1 import x as x

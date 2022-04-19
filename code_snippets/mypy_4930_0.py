from mypackage.submod1 import *     # * -> HELLO and error goes away
from mypackage.submod2 import greet # comment out and error goes away
__all__ = ['HELLO', 'greet'] # does nothing

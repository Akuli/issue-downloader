# sup/bro.py - This is the object we want to be available at the top level
__all__ = ["Bro"]

class Bro:
    pass

# sup/__init__.py - This brings the Bro object to the sup module level
from . import bro
from .bro import *

__all__ = bro.__all__

# __init__.py - This brings the sup module, including the Bro object, to the top module level
from .sup import *

# cool.py - This file uses the Bro object in a function
import gym

__all__ = ["story"]

def story() -> gym.Bro:
    return gym.Bro()

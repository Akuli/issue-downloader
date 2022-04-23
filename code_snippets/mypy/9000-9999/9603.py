# -*- coding: utf-8 -*-
from typing import Any, Dict, Optional

class Base(object):
    """Base class to demonstrate issue."""

    def func(self, *args, **kwargs) :
        """Do nothing."""
        reveal_type(self.func) # note: Revealed type is 'def (*args: Any, **kwargs: Any) -> Any'

class Derived1(Base):
    def func(self, myobj): # No Error
        """Override."""
        reveal_type(self.func) # note: Revealed type is 'def (myobj: Any) -> Any'

class Derived2(Base):
    def func(self, myobj) -> Any: # error: Signature of "func" incompatible with supertype "Base"
        """Override."""
        reveal_type(self.func) # note: Revealed type is 'def (myobj: Any) -> Any'


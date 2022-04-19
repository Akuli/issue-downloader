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


[mypy]
allow_redefinition = False
check_untyped_defs = True
disallow_any_explicit = False
disallow_any_generics = True
disallow_untyped_calls = True
ignore_errors = False
ignore_missing_imports = True
implicit_reexport = True
local_partial_types = True
strict_optional = True
strict_equality = True
no_implicit_optional = True
warn_no_return = True
warn_unused_ignores = True
warn_redundant_casts = True
warn_unused_configs = True
warn_unreachable = True

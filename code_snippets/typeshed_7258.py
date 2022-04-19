import logging

class C:
    def __init__(self) -> None:
        self.level = logging.INFO

    def enable_debug(self) -> None:
        # Error: expression has type "Literal[10]", variable has type "Literal[20]"
        self.level = logging.DEBUG

import logging

class Base:
    level = logging.INFO

class Derived(Base):
    level = logging.DEBUG  # Error -- incompatible with base class

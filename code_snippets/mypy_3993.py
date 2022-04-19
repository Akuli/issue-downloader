from typing import *

class Foo:
    class Bar:
        pass

    def __init__(self) -> None:
        self._bar = None

    def start(self) -> None:
        self._bar = self.Bar()

self._bar = None  # type: Bar

self._bar = None  # type: self.Bar


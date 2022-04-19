from typing import NamedTuple

class First(NamedTuple):
    def method(self):
        pass

class Second(NamedTuple):
    recursive: 'Second'

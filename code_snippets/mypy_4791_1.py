from typing import Union
class C:
    def m(self) -> Union[bool, type(NotImplemented)]:
        return NotImplemented

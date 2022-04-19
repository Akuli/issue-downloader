from typing import Any, Optional


class Foo(object):
    def __init__(self):
        # type: () -> None
        self.x = 0

    def get_x(self, a=None, b=None):
        # type: (Optional[int], Optional[int]) -> int
        return self.x + (a or 0) + (b or 0)


def get_x_patch(self, *args, **kwargs):
    #  type: (Foo, *Any, **Any) -> int
    return 42


Foo.get_x = get_x_patch

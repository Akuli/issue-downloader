from functools import partial
from typing import Any, Callable, Union

yesno = True

thingy: Union[Callable, int]
reveal_type(thingy)
if yesno:
    thingy = partial(isinstance, "foo")
    reveal_type(thingy)
else:
    thingy = 42
reveal_type(thingy)

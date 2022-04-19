from typing import Hashable


class SomeDClass:
    __hash__: None = None  # type: ignore

d = {
    [1]: 1,  # SUS ALERT! fails at runtime
    SomeDClass(): 2,  # SUS ALERT! fails at runtime
}

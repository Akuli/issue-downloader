from typing import Dict, Optional, Tuple
import numpy as np

class Meta(type):
    def __new__(
        cls, name: str, bases: Tuple[type, ...], dct: Dict, *args,
        a: Optional[int] = None, **kwargs
    ):
        return super().__new__(cls, name, bases, dct, *args, **kwargs)

class A(np.ndarray, a=1, metaclass=Meta):
    pass

a = A(shape=(2,))

import os
from typing import AnyStr

def thing(value: AnyStr) -> None:
    with os.scandir(value) as it:
        for file in it:
            if file.name.endswith('.xml'): ...

thing("hello")
#thing(b"world")

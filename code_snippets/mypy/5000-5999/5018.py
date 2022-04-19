# file default_config.py
timeout = 100
one_flag = True
other_flag = False

# file __main__.py
import default_config
from typing import Protocol

class Options(Protocol):
    timeout: int
    one_flag: bool
    other_flag: bool

def setup(options: Options) -> None:
    ...

setup(default_config)  # OK

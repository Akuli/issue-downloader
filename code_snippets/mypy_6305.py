import re
from typing import Optional, Any


def test(y: Optional[str]) -> Any:
    if y:
        return lambda x: not re.search(y,x) # This is fine

def test2(y: Optional[str]) -> Any:
    if y:
        return filter(lambda x: not re.search(y,x), ["1", "2"]) #raises an error

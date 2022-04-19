from typing import Optional, List

class Foo:
    def __init__(self):
        self.bar: Optional[str] = None

    def barsplit(self) -> List[str]:
        if not self.bar:
            raise ValueError
        return self.bar.split()

from typing import List, Optional, Callable
from functools import wraps

def require_bar(method: Callable) -> Callable:
    @wraps(method)
    def decorated_method(self, *args, **kwargs):
        if not self.bar:
            raise ValueError
        return method(self, *args, **kwargs)

    return decorated_method

class Foo:
    def __init__(self):
        self.bar: Optional[str] = None

    @require_bar
    def get_barsplit(self) -> List[str]:
        return self.bar.split()


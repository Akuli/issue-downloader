from typing import Optional, List

class Foo:
    def __init__(self):
        self.bar: Optional[str] = None

    def barsplit(self) -> List[str]:
        if not self.bar:
            raise ValueError
        return self.bar.split()

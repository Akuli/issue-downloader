from typing import Callable

class Test:
    def method1(self) -> None:
        pass

    def method2(self, optional: int = 0) -> None:
        pass

    def test(self, something: bool) -> None:
        action: Callable[[], None]
        action = self.method1 if something else self.method2

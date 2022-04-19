from typing import Any

class A:
    doc = ""

class B(A):
    # remove "-> Any" to make mypy happy
    @property
    def doc(self) -> Any:
        return ""

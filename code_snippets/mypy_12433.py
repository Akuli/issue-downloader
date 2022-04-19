from typing import Protocol
from unittest.mock import create_autospec
from abc import abstractmethod


class A(Protocol):
    @abstractmethod
    def method(self) -> int:
        raise NotImplementedError

    class Error:  # if commenting this class
        pass      # mypy works without complains

def test_one() -> None:
    p = create_autospec(A, instance=True)

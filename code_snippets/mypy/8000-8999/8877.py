from typing import TypeVar, Generic
from abc import abstractmethod, ABC

K = TypeVar('K')


class Metric(ABC, Generic[K]):

    @abstractmethod
    def sum(self, other: "Metric[K]") -> "Metric[K]":
        pass


class MyFloatMetric(Metric[float]):
    def sum(self, other: "MyFloatMetric") -> "MyFloatMetric":
        return MyFloatMetric()

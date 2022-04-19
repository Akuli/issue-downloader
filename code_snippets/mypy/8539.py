from abc import abstractmethod
from functools import total_ordering

@total_ordering
class PriorityMixin:

    @abstractmethod
    def getName(self) -> str: ...

    @abstractmethod
    def getPriority(self) -> int: ...

    def __hash__(self) -> int:
        return hash(self.getName())

    def __eq__(self, other: object) -> bool:
        if isinstance(other, PriorityMixin):
            return self.getName() == other.getName()
        else:
            return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, PriorityMixin):
            prioCmp = self.getPriority() - other.getPriority()
            if prioCmp == 0:
                return self.getName() < other.getName()
            else:
                return prioCmp < 0
        else:
            return NotImplemented

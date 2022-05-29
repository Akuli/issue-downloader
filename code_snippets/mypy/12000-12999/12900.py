from typing import List, Iterable


class Member:
    pass


class Group:
    @property
    def members(self) -> List[Member]:
        pass

    @members.setter
    def members(self, members: Iterable[Member]) -> None:
        pass


group = Group()
group.members = {Member(), Member()}

# mypy error: test.py:19: error: Incompatible types in assignment (expression has type "Set[Member]", variable has type "List[Member]")

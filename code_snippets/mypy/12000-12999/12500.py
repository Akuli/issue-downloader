import dataclasses
from typing import TypeVar, Generic


class Parent:
    pass


class Daughter(Parent):
    pass


class Son(Parent):
    pass


RestrictedChild = TypeVar("RestrictedChild", Daughter, Son)
TupleChildrenX2 = tuple[RestrictedChild, RestrictedChild]


@dataclasses.dataclass
class ContainerWithAlias(Generic[RestrictedChild]):

    children: TupleChildrenX2
    reveal_type(children)


@dataclasses.dataclass
class ContainerNoAlias(Generic[RestrictedChild]):

    children: tuple[RestrictedChild, RestrictedChild]


container_with_alias = ContainerWithAlias[Daughter](children=(0, 0))  # No type checking (unexpected)
container_no_alias = ContainerNoAlias[Daughter](children=(0, 0))  # Error as expected

container_with_alias_unbound = ContainerWithAlias(children=(0, 0))  # No type checking (unexpected)
container_no_alias_unbound = ContainerNoAlias(children=(0, 0))  # Error as expected

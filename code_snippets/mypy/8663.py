from typing import NamedTuple, Optional

class BaseInventory(NamedTuple):
    number: Optional[int]
    name: str


class Inventory(BaseInventory):
    number: int


item = Inventory(42, 'parrot')
item.number % 10  # mypy allows this
number, _ = item
number % 10  # mypy does not allow this

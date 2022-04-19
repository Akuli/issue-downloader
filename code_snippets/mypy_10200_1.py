import dataclasses
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .myclass import MyClass


@dataclasses.dataclass
class MyDataclassBase:
    my_field: Optional['MyClass']

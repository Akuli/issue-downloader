# type: ignore[misc] # Ignores 'Any' input parameter
from typing import Any, Iterable

JsonSerializable = Any
CsvSerializable = Iterable[Any]

from my_app.typing import JsonSerializable

def foo(data: JsonSerializable) -> None:
    ...

from typing import Any, Iterable

JsonSerializable = Any  # type: ignore[misc] # Ignores 'Any' input parameter
CsvSerializable = Iterable[Any]  # type: ignore[misc] # Ignores 'Any' input parameter

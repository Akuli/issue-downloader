# pep249.py

from typing import Any
from typing_extensions import Protocol, runtime_checkable

@runtime_checkable
class Connection(Protocol):
    def close(self) -> None: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
    def cursor(self, *__args: Any, **__kwargs: Any) -> Any: ...

# main.py

from typing import Generic, TypeVar
import pep249
import pymysql

ConnectionT = TypeVar("ConnectionT", bound=pep249.Connection)

class DatabaseAdapter(Generic[ConnectionT]): ...

class MySQLAdapter(DatabaseAdapter[pymysql.connections.Connection]): ...


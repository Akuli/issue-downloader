# main.py

from typing import Generic, TypeVar
import pep249
import pymysql

ConnectionT = TypeVar("ConnectionT", bound=pep249.Connection)

class DatabaseAdapter(Generic[ConnectionT]): ...

class MySQLAdapter(DatabaseAdapter[pymysql.connections.Connection]): ...

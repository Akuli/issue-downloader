from typing import Any

isinstance(1, str | Any)  # no error, fails at runtime with TypeError: typing.Any cannot be used with issubclass()

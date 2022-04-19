# NoReturn was introduced in Python 3.6.5.
if TYPE_CHECKING:
	from typing_extensions import NoReturn
else:
	NoReturn = None

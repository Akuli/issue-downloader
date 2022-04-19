from typing import Any, Generic, overload, TypeVar, TYPE_CHECKING
import numpy as np

_CharType = TypeVar("_CharType", np.str_, np.bytes_)


class CharArray(Generic[_CharType]):
    @overload
    def strip(self: CharArray[np.str_], chars: str = ...) -> CharArray[np.str_]: ...
    @overload
    def strip(self: CharArray[np.bytes_], chars: bytes = ...) -> CharArray[np.bytes_]: ...


ar_any: CharArray[Any]
ar_str: CharArray[np.str_]
ar_bytes: CharArray[np.bytes_]

if TYPE_CHECKING:
    # The good
    reveal_type(ar_str.strip())  # E: Revealed type is "__main__.CharArray[numpy.str_]"
    reveal_type(ar_bytes.strip())  # E: Revealed type is "__main__.CharArray[numpy.bytes_]"

    # The bad
    # "__main__.CharArray[Any]" would be expected here due to overload ambiguity
    reveal_type(ar_any.strip())  # E: Revealed type is "__main__.CharArray[numpy.str_]"

    # Calling the method directly from the class does do the trick
    reveal_type(CharArray.strip(ar_any))  # E: Revealed type is "test.CharArray[Any]"

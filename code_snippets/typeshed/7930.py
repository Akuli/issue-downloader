import hmac
import hashlib
hmac.digest(b"123", b"msg", hashlib.sha256)  # 3: error: Argument 3 to "digest" has incompatible type "Callable[[Union[bytes, Union[bytearray, memoryview, array[Any], mmap, _CData]], DefaultNamedArg(bool, 'usedforsecurity')], _Hash]"; expected "str" [arg-type]

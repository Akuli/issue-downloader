foo: bytes = bytearray()
assert isinstance(foo, bytes)

class bytes(ByteString):
    ...

class bytearray(MutableSequence[int], ByteString):
    ...


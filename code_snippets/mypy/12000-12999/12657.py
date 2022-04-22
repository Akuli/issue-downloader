
def f(data: ByteString) -> str:
    if not isinstance(data, bytes):
        data = bytes(data)

    return data.decode()

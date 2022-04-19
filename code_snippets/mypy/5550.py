def ensure_native_str(str_or_bytes):  # type: (Union[Text, bytes]) -> str
    return (
        str_or_bytes if isinstance(str_or_bytes, str) else
        str_or_bytes.decode('utf-8') if six.PY3 else
        str_or_bytes.encode('utf-8')
    )

def ensure_native_str(str_or_bytes):  # type: (Union[Text, bytes]) -> str
    if isinstance(str_or_bytes, str):
        return str_or_bytes
    if six.PY3:
        return str_or_bytes.decode('utf-8')
    return str_or_bytes.encode('utf-8')

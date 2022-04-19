def read(msg: Union[Message[str], Message[bytes]]) -> None:
    msg.content.method_in_neither_str_nor_bytes()

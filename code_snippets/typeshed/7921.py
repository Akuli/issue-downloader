import io
stream = io.TextIOWrapper(io.BytesIO(b'"")\r\nx\r\n'))
stream.read(1)
stream.read(1)
stream.read(1)
print('-----> tell:', stream.tell())

def _upgrade_high_scores_file(file: IO[str], old_version: int) -> None:
    ...
    file.seek(len(b"catris high scores file v"))
    ...

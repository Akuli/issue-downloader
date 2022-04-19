def bad_reader(path: str) -> bytes:
    if path == "bad":
        raise PermissionError

    with open(path, "rb") as f:
        return f.read()


def load_data(path: str) -> bytes:
    try:
        return bad_reader(path)
    except OSError:
        print("OSError caught")
    except PermissionError:
        # This branch will never be hit, since `OSError` will always catch
        # permission error
        print("PermissionError caught")

    return b""


load_data("bad")

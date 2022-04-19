def export_file(src: str) -> str:
    with open(src) as f:
        data = f.read()
    return data

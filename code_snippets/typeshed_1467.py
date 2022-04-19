# _txt_fmt is a object gotten from `re.compile`
with open(file, 'r+') as f:
    with mmap.mmap(f.fileno(), 0) as data:
        match = _txt_fmt.match(data)

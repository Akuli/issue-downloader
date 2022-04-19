m = re.search(pattern, string)
if m:
    return m.group(group)

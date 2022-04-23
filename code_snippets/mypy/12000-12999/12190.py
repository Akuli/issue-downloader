if m := re.search(pattern, string):
    return m.group(group)

m = re.search(pattern, string)
if m:
    return m.group(group)

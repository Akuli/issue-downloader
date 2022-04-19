a = None
for b in [1, 2]:
    if a is None:
        a = b
        continue
    print("hi")  # false unreachable error

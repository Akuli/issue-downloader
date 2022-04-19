x = []
for s in 'x', 'y':
    if 1 in x:  # No error, but should be
        x.append(s)

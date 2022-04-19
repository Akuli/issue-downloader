dct = {"": ""}

# ok
trans = str.maketrans(dct)
"".translate(trans)

# err
"".translate(str.maketrans(dct))

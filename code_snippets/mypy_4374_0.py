mac_value = int(mac.translate(str.maketrans(dict([(x, None) for x in [" ", ".", ":", "-"]]))), 16)

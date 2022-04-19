mac_value = int(mac.translate(str.maketrans(dict([(x, None) for x in [" ", ".", ":", "-"]]))), 16)

trans = str.maketrans(dict([(x, None) for x in [" ", ".", ":", "-"]]))
mac_value = int(mac.translate(trans), 16)

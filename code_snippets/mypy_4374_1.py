trans = str.maketrans(dict([(x, None) for x in [" ", ".", ":", "-"]]))
mac_value = int(mac.translate(trans), 16)

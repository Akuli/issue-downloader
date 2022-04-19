h = hashlib.sha1()
pickle.dumps(obj, protocol=5, buffer_callback=h.update)

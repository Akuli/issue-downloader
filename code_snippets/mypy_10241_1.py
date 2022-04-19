from tempfile import mkstemp
_, temp_path = mkstemp()
reveal_type(temp_path) # str?

import tempfile

with tempfile.NamedTemporaryFile() as file:
    reveal_type(file) # tempfile._TemporaryFileWrapper[builtins.bytes]
    file.asdfasdf # no error

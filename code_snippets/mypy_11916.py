import sys

if sys.version_info < (3, 8, 0):
    import importlib_metadata as metadata
else:
    from importlib import metadata

my_metadata = metadata.metadata("mypy")  # just using mypy as an example here; could be any package's name

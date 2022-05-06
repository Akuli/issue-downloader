from typing import TypedDict


class MyTypedDict(TypedDict, total=False):
    param1: int
    param2: str

td: MyTypedDict = {"param1": 2, "param2": "foo"}
td.pop("param1")
td.clear()

# The following options are set by the --strict command line flag
warn_unused_configs=True
disallow_any_generics=True
disallow_subclassing_any=True
disallow_untyped_calls=True
disallow_untyped_defs=True
disallow_incomplete_defs=True
check_untyped_defs=True
disallow_untyped_decorators=True
no_implicit_optional=True
warn_redundant_casts=True
warn_unused_ignores=True
warn_return_any=True
no_implicit_reexport=True
strict_equality=True
# End of --strict options

ignore_missing_imports=True
show_error_codes=True

plugins=pydantic.mypy, numpy.typing.mypy_plugin

from mypy_extensions import TypedDict

GroupDataDict = TypedDict(
    'GroupDataDict', {"children": str,
                      "vars": str,
                      "hosts": str}, total=False
)

test_group: GroupDataDict = {}
key = "children"
if key in ("children", "vars"):
    test_group[key] = "a"

if key not in ["children", "vars"]:
    raise ValueError("")
test_group[key] = "b"

print(test_group)

[mypy]
python_version = 3.7

check_untyped_defs = True
disallow_any_generics = True
disallow_untyped_calls = True
ignore_errors = False
ignore_missing_imports = True
strict_optional = True
warn_unused_ignores = True
warn_redundant_casts = True
warn_unused_configs = True


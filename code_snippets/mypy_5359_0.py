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

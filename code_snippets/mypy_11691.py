foo: dict[type, str] = {int: ""}

{**foo, str: ""}
# mypy seems to interpret it as this, where the error makes sense:
{str: ""}.update(foo)

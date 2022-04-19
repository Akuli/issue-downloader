# mypy: disable-error-code=name-defined python-verion="3.6"

a  # error: Name "a" is not defined  [name-defined]

[[tool.mypy.overrides]]
module  = ["test"]
disable_error_code = "name-defined"
python_verion="3.6"

# mypy: AMONGUS


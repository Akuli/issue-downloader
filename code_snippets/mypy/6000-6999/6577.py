TestOne = TypedDict('TestOne', {'test': int, 'another': str}, total=False)
TestTwo = TypedDict('TestTwo', {'test': int}, total=False)

var_1: TestOne = {'test': 1, 'another': 'hi'}
var_2: TestTwo = var_1  # Doesn't cause a type error... why not?? 'another' is not a valid key on a TestTwo
var_3: TestTwo = {  # Does cause a type error, correctly. "Extra key 'another' for TypedDict 'TestTwo'"
    'test': 2, 'another': 'hi'
}

TestThree = TypedDict('TestThree', {'test': int}, total=False)
TestFour = TypedDict('TestFour', {'test': int, 'another': str}, total=False)
var_4: TestThree = {'test': 3}
var_5: TestFour = var_4  # Causes a type error.... WHY???? "Incompatible types in assignment (expression has type "TestThree", variable has type "TestFour")"

[mypy]
plugins = sqlmypy
disallow_untyped_calls = False
disallow_untyped_defs = True
ignore_missing_imports = True
warn_return_any = False
follow_imports = silent
allow_redefinition = True


@given("I am on the main page")
def step_impl(context):
    pass


@when("I type login and password")
def step_impl(context):
    pass


@then("I am logged in")
def step_impl(context):
    pass

[mypy]
python_version = 3.6
allow_redefinition = True
ignore_missing_imports = True
check_untyped_defs = False

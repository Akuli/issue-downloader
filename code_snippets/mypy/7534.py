[mypy]
plugins = mypy_django_plugin.main
warn_return_any = True
warn_unused_configs = True
disallow_subclassing_any = True
disallow_any_generics = True
disallow_untyped_calls = True
disallow_untyped_defs = True
disallow_incomplete_defs = True
check_untyped_defs = True
disallow_untyped_decorators = True
no_implicit_optional = True
warn_redundant_casts = True
warn_unused_ignores = True
mypy_path = stubs

[mypy.plugins.django-stubs]
django_settings_module = "imake.settings"

('', '', 2)


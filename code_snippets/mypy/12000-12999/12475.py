[mypy]
ignore_missing_imports = True
color_output = True
pretty = True
show_error_codes = True
check_untyped_defs = True
warn_unreachable = True
error_summary = True
# https://github.com/python/mypy/issues/9091
no_implicit_optional = True

# pip install sqlalchemy2-stubs
plugins = sqlalchemy.ext.mypy.plugin

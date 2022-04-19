import sys
import mypy

mypy.util.check_python_version("stubgen")

options = mypy.stubgen.Options(
  pyversion=sys.version_info[:2],
  no_import=False,
  doc_dir="",
  search_path="",
  interpreter="",
  ignore_errors=False,
  include_private=False,
  output_dir="out",
  modules=[],
  packages=["gdb"],
  files=[],
  verbose=False,
  quiet=False,
  export_less=False
)

mypy.stubgen.generate_stubs(options)

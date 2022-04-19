# src/foo.py
from mypy.api import run

_, _, exit_code = run(["--install-types", "--non-interactive", "src"])
assert exit_code == 0

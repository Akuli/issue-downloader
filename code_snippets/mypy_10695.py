from typing import Any
test: Any[int,str] = "Test"
print(test)

[mypy]
python_version = 3.8
ignore_missing_imports = True


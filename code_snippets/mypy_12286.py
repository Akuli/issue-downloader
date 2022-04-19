import sys
if sys.version_info < (3, 11):
    print(21 + "sus")  # very funny, but is a type error 😢
if sys.platorm == "win32":
    print(21 + "sus")  # very funny, but is a type error 😢

[tool.mypy]
platforms = ["lignux", "darwin", "win32"]
python_versions = [3.11, 3.10, 3.9, 3.8, 3.7]


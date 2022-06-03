import sys, winreg

if sys.platform == "win32":
    winreg.QueryValueEx

# Success: no issues found in 1 source file

# mypy: platform=win32
import sys, winreg

if sys.platform == "win32":
    winreg.QueryValueEx  # test.py:5:5: error: Module has no attribute "QueryValueEx"  [attr-defined]

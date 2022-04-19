# good.py

import sys
assert sys.platform == "win32"

from ctypes import WINFUNCTYPE, windll, WinError, get_last_error

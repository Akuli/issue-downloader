import sys
assert sys.platform == 'win32'

from sys import platform
assert platform == 'win32'

# good.py

import sys
assert sys.platform == "win32"

from ctypes import WINFUNCTYPE, windll, WinError, get_last_error

# bad.py

from sys import platform
assert platform == "win32"

from ctypes import WINFUNCTYPE, windll, WinError, get_last_error

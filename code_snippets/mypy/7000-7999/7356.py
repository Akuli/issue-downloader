import sys
try:
    f = open('.', 'rb')
except PermissionError if sys.platform == "win32" else ():
    pass

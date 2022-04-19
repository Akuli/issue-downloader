import sys

# This causes the error
try:
    raise Exception
except Exception:
    ex, val, _ = sys.exc_info()
    print(f"Failed: {ex.__name__}: {val}")  # Line 8

# This does not
try:
    raise Exception
except Exception:
    ex, val, _ = sys.exc_info()
    if ex is not None:  # Pointless comparison
        print(f"Failed: {ex.__name__}: {val}")

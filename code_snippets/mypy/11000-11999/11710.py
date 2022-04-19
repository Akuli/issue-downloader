import sys

import foo

sys.modules["bar"] = sys.modules["foo"]

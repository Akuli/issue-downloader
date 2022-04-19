try:
    from inspect import isawaitable  # py35+
except ImportError:
    from backports_abc import isawaitable

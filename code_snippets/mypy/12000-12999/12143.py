class A(TypedDict):
    """Empty"""

a: A = {}
reveal_type(a.get("foo", None))

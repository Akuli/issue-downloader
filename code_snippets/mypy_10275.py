class A(MutableMapping[str, Any]): pass
def something() -> A: pass
something() == {}

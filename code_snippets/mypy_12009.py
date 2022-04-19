class A: pass
class B: pass
class C:
    attr: A | B | None

c = C()
if c.attr is None: pass
elif isinstance(c.attr, A): pass
elif isinstance(c.attr, B): pass  # Optional line - no difference if removed
reveal_type(c.attr)

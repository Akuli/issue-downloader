# inner class before its use
class Outer(Base):
  class Inner: pass
  field: Outer.Inner
class Base: pass

# base before its use
class Base: pass
class Outer(Base):
  field: Outer.Inner
  class Inner: pass

# no base
class Outer:
  field: Outer.Inner
  class Inner: pass

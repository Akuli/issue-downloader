class Outer(Base):
  field: Outer.Inner  # E: Name 'Outer.Inner' is not defined
  class Inner: pass
class Base: pass

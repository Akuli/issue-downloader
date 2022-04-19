class Foo:
    pass

Base = Foo

class Types:
    Base = Foo

reveal_type(Base)
reveal_type(Types.Base)

class Works(Base):
    pass

class Fails(Types.Base):
    pass

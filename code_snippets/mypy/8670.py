from sqlalchemy import Column, Integer

class Foo(Base):
    oid = Column(Integer, primary_key=True)

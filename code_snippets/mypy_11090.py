class OrmBase:
    pass

class Orm1(OrmBase):
    pass

class Orm1Prime(OrmBase):
    pass

class Orm2(OrmBase):
    pass

class Orm2Prime(OrmBase):
    pass

def func(orm: Union[Orm1, Orm2]):
    orm_mapper = {
        Orm1: Orm1Prime, 
        Orm2: Orm2Prime,
    }
    mapped: Union[Type[Orm1Prime], Type[Orm2Prime]] = orm_mapper[orm.__class__]
    # Incompatible types in assignment (expression has type "Type[OrmBase]",
    # variable has type "Union[Type[Orm1Prime], Type[Orm2Prime]]") [E]
    return mapped

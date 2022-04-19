def deco(value) -> int:
    ...
    
@deco
class Class:
    ...
    
reveal_type(Class) # note: Revealed type is "def () -> __main__.Class"

@deco
def function(): ...

reveal_type(function) # note: Revealed type is "builtins.int"

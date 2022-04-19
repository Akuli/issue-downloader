class Some(Enum):
   a = 1
   b = 2
   _ignore_ = ('a',)

reveal_type(Some.a) # E: "Type[Some]" has no attribute "a"

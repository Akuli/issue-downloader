x: Optional[A]

reveal_type(x)  # N: Revealed type is "Optional[A]"

x = getA()
reveal_type(x) # N: Revealed type is "Optional[A]"

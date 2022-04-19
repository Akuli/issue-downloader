x: Union[int, str] = 'a'
x = x + 1 # error
reveal_type(x)  # Revealed type: int

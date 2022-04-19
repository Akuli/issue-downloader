mapping: Dict[str, str] = {"a": "x"}
val: Optional[str] = None
val = "a"
reveal_type(val) # Revealed type is "builtins.str"
val = mapping[val] if val in mapping else val
reveal_type(val) # Revealed type is "builtins.str"
val = mapping.get(val, val)
reveal_type(val) # Revealed type is "Union[builtins.str, None]"

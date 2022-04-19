lst1 = [1, 'a', None]
lst2 = [1, None, 'a']

reveal_type(lst1) # builtins.list[builtins.object*]
reveal_type(lst2) # builtins.list[Union[builtins.str, builtins.int, builtins.None]]

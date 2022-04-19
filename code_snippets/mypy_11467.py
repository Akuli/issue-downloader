type  # no error
t1 = type  # error: Expression type contains "Any" (has type "Type[type]")
t2: type[type] = type  # no error  
t3: Type[type] = type  # no error

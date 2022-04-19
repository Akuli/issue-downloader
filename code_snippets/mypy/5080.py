try:
    raise Exception()
except Exception as e:
    pass
e = 4  # error: Assignment to variable 'e' outside except: block

# 1)
os.getenv('VARNAME') | flatmap(lambda m: m.upper())

# 2)
flatmap(os.getenv('VARNAME'), lambda m: m.upper())

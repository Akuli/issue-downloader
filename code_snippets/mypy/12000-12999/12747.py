def f():
	print(x)
	x = 2
	global x
	print(y)
	global y
def f2():
	x = y = 0
	def g():
		print(x)
		x = 2
		nonlocal x
		print(y)
		nonlocal y

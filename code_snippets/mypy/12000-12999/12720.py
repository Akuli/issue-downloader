NICE_LIST =  [
		(1, 2),
		(4, 5),
	]
BAD_LIST =  [
		(1, 2, 'I am bad'),
		(4, 5),
	]

PROCESS_NICE = [(x[1], range(x[0]), ['something' for _ in range(x[1])])
	for x in NICE_LIST]
PROCESS_BAD = [(x[1], range(x[0]), ['something' for _ in range(x[1])])
	for x in BAD_LIST]

reveal_locals()

#! /usr/bin/env python

from typing import Dict, List, Union

def main(arg):
	# type: (bool) -> Union[Dict[str, str], List[str]]

	if arg:
		var = list()
		var.append('something')
	else:
		var = dict()
		var['key'] = 'something'

	return var


if __name__ == '__main__':
	main(True)

import sys
from typing import Optional

found_id = None

symbols_list = [{'symbol': 'A', 'id': 1}, {'symbol': 'B', 'id': 2},  {'symbol': 'B', 'id': 3}]

for entry in symbols_list:
    if entry['symbol'] == 'B':
        if found_id:
            print('error, symbol found multiple times!')
            sys.exit(1)

        found_id = entry['id']

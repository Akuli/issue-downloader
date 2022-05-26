import csv
from io import StringIO

csvtext = "foo,bar\n1,2\n3,4,5"

csvreader = csv.DictReader(StringIO(csvtext), delimiter=',')

#def checkrow(row: dict[str | None, str]) -> None:
def checkrow(row: dict[str, str]) -> None:
	if None in row:
		print(f"None found as key with value {row[None]!r}, someone broke a promise!")

for row in csvreader:
	print(row)
	checkrow(row)

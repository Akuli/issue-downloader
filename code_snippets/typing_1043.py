import argparse
parser = argparse.ArgumentParser(description="My parser")
parser.add_argument("--my_bool", type=bool)
print(parser.parse_args())  # Error: statement is unreachable

import argparse
parser = argparse.ArgumentParser(description="My parser")
parser.add_argument("--my_bool", type=bool)  # Error: type=bool doesn't work, see https://stackoverflow.com/q/15008758
print(parser.parse_args())

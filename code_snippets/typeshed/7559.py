import argparse

class CSVCallback(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, list(values.split(',')))

parser = argparse.ArgumentParser()
parser.add_argument('-o', action=CSVCallback, default=[])

args = parser.parse_args()

def csv_callback(value: str) -> list[str]:
    return list(value.split(','))

parser.add_argument('-o', type=csv_callback, default=[])

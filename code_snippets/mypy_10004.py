import json
import pathlib
import tempfile
import textwrap
import time

from mypy import api


def generate_n_overloads(n: int, types=('str', 'int', 'float')) -> str:
    result = ['import typing']

    for name_count in range(n):
        type_name = types[name_count % len(types)]
        name = f'overload_{name_count}_{type_name}'
        annotation = (
            textwrap.dedent(f'''
        @typing.overload
        def get_param(param: typing.Literal['{name}']) -> {type_name}: ...
        ''')
        )
        result.append(annotation)
    return '\n'.join(result)


def build_test_case(dest_dir: pathlib.Path, n_overloads: int) -> pathlib.Path:
    pkg_dir = dest_dir / 'example_overloads_pkg'
    pkg_dir.mkdir(exist_ok=True)
    stubfile = pkg_dir / '__init__.pyi'
    stubfile.write_text(generate_n_overloads(n_overloads))

    pkg_file = pkg_dir / '__init__.py'
    pkg_file.write_text('def get_param(param): ...')

    test_script = dest_dir / 'script.py'
    test_script.write_text(textwrap.dedent('''
        from example_overloads_pkg import get_param
        
        get_param('overload_3_str').upper()  # Good
        get_param('overload_2_float').upper()  # Bad
    '''))
    return test_script


if __name__ == '__main__':
    tmpdir = tempfile.TemporaryDirectory()

    scale_times = {}
    numbers_to_check = [16, 32, 64, 128, 256, 512, 1024]
    # numbers_to_check = [16, 32, 64, 128, 256, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 8000, 10000]
    for number_of_overloads in numbers_to_check:
        print(f'Overload size: {number_of_overloads}')
        test_script = build_test_case(pathlib.Path(tmpdir.name), number_of_overloads)
        start = time.perf_counter()
        result = api.run([str(test_script)])
        end = time.perf_counter()
        elapsed = end - start

        print(' Time:', end - start)
        if scale_times:
            last_n = next(reversed(scale_times))
            print(f" Slowdown: x{elapsed / scale_times[last_n]:.2f}")
        scale_times[number_of_overloads] = elapsed

    # Save the times to json for plotting/analysis.
    with open('times.json', 'wt') as fh:
        json.dump(scale_times, fh)


import json

import matplotlib.pyplot as plt
import numpy as np


with open('times.json', 'rt') as fh:
    times = json.load(fh)

n_points, times = zip(*times.items())

n_points = np.array(n_points, dtype=int)
times = np.array(times)
fit = np.polyfit(n_points, times, 2)
p = np.poly1d(fit)

plt.title('Number of overloads vs execution time of mypy')

plt.xscale('log')
plt.yscale('log')


plt.scatter(n_points, times)
plt.xlabel('Number of overloads')
plt.ylabel('Time to run mypy / seconds')
plt.show()


{"16": 0.11653269396629184, "32": 0.13803347101202235, "64": 0.1889677940052934, "128": 0.42529276601271704, "256": 1.4768535409821197, "300": 2.165687720000278, "400": 3.581374307977967, "500": 5.615040614036843, "600": 8.182245634961873, "700": 10.219899011019152, "800": 14.204097100009676, "900": 19.01026200200431, "1000": 21.914704270020593, "1500": 50.26287814299576, "2000": 88.03798637498403, "2500": 140.229756515997, "3000": 206.8722462329897, "4000": 373.4201490940177, "5000": 596.6820141010103, "6000": 831.5039637690061, "8000": 1579.1185438489774, "10000": 2624.7711193099967}

import typing

@typing.overload
def get_param(param: typing.Literal['some_float']) -> float: ...


@typing.overload
def get_param(param: typing.Literal['some_other_int']) -> int: ...


@typing.overload
def get_param(param: typing.Literal['further_str']) -> str: ...



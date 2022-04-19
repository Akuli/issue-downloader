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


# Olga rozhdestvina

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1.0, 10.0, 1000)
y1 = x * x
y2 = x * x * x

fig, ax = plt.subplots()
ax.plot(x, y1, label="x squared")
ax.plot(x, y2, label="x cubed")
ax.legend()
fig.show()

input()
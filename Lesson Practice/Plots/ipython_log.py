# IPython log file

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1.0, 100.0, 100)
y1 = x**2
y2 = 2**x
plt.legend()
plt.title("Hello, World!")
plt.xlabel("Hello, X!")
plt.ylabel("Hello, Y!")


plt.plot(x, y1, "g.", label = "squared")
plt.plot(x, y2, "r.", label = "exponential")
plt.plot(x, np.log(y1), "g.", label = "squared")
plt.plot(x, np.log(y2), "r.", label = "exponential")

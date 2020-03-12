# Olga Rozhdestvina
# This program displays a plot of the functions 
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,4)

def f(x):
    return x
def g(x):
    return x**2
def h(x):
    return x**3

#plot the function
functions = [f, g, h]
for func in functions:
    plt.plot(func(x))
    plt.title("A Plot of Functions")
    #labelling through legend function taken from https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html
    plt.legend([('f(x)'), ('g(x)'), ('h(x)')])

#show the plot
plt.show() 
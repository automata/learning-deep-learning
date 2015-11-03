import pylab as py
import numpy as np

def sigmoid(z):
    return 1. / (1 + np.exp(-z))

def step(z):
    if z <= 0:
        return 0.
    else:
        return 1.

n = 100
xs = np.linspace(-10, 10, n)

py.plot(xs, sigmoid(xs), 'bo')
py.plot(xs, [step(x) for x in xs], 'r-')
py.xlabel('x')
py.ylabel('y')
py.title('Sigmoid x step functions')
py.show()

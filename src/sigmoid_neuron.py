import numpy as np

# A Sigmoid neuron is a type of neuron that uses a sigmoid function as an
# activation function (Perceptron uses a step function instead).

# See sigmoid_curve.py to understand how more smooth is sigmoid when compared
# with step function.

# Using different activation functions f(w * x + b) will make changes on
# the partial derivatives (that we use to change values of w and b, smoothly).
# Because sigmoid function has a exponential, and exponentials have sweet
# properties while derivated, we're going to use them a lot as activation
# functions.

class Sigmoid:
    def __init__(self, w, x, bias):
        self.w = np.array(w)
        self.x = np.array(x)
        self.bias = bias

    def sigma(self, z):
        sum_ = 0
        for j in xrange(self.w.size):
            sum_ += self.w[j] * self.x[j] - self.bias
        return 1.0 / (1.0 + np.exp(-sum_))

    def run(self):
        return self.sigma(self.w.dot(self.x) + self.bias)

sigmoid = Sigmoid([0.5, 0.5], [0, 1], 3.0)
print sigmoid.run()

import numpy as np

# We can rewrite the Perceptron model as a dot product between two vectors,
# one for weights and other for inputs. And we can pass the threshold to
# the other side of the equation.

# Bias: how much easy is a Perceptron to _fire_ or to output 1.
# It's the inverse of threshold, so bias = -threshold.

class Perceptron:
    def __init__(self, w, x, bias):
        self.w = np.array(w)
        self.x = np.array(x)
        self.bias = bias

    def run(self):
        prod = self.w.dot(self.x) + self.bias
        if prod <= 0:
            return 0
        else:
            return 1

neuron = Perceptron([6.0, 2.0, 2.0], [0, 1, 0], 5.0)
print neuron.run()

# We can use a Perceptron to simulate logical operations, like an NAND:

nand = Perceptron([-2, -2], [0, 0], 3)
print "0 NAND 0 = %s" % nand.run()
nand = Perceptron([-2, -2], [0, 1], 3)
print "0 NAND 1 = %s" % nand.run()
nand = Perceptron([-2, -2], [1, 0], 3)
print "1 NAND 0 = %s" % nand.run()
nand = Perceptron([-2, -2], [1, 1], 3)
print "1 NAND 1 = %s" % nand.run()

# We can create any logical operation, including a bitwise sum:

x1 = 1
x2 = 1
w = [-2, -2]
bias = 3
nand1 = Perceptron(w, [x1, x2], bias)
nand2 = Perceptron(w, [x1, nand1.run()], bias)
nand3 = Perceptron(w, [x2, nand1.run()], bias)
nand4 = Perceptron(w, [nand1.run(), nand1.run()], bias)
nand5 = Perceptron(w, [nand2.run(), nand3.run()], bias)
print '%s BITWISE SUM %s = %s with carry bit %s' % (
    x1,
    x2,
    nand5.run(),
    nand4.run())

# Now we know that we can use a neuron to tweak the input of other. Well,
# we can do the same for weights and bias: we can use a neuron to tweak weight
# and bias values of other neurons. That's the base for machine learning: we
# call the algorithms that control such weight tweaks as learning algorithms.
# Those algorithms will "learn" how to adjust weights and bias to produce the
# right output for the given inputs.

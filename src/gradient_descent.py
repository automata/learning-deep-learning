# We can use calculus to find global minima of C analytically: we can
# calculate the extremes of C with derivatives. However, that only works with
# functions of few variables. So, calculus can't help us.

# We can think C as a surface, and a ball should go down that surface, stopping
# at the minimum height place.

# We can use a gradient vector to simulate the movement of a ball, forcing
# it to only go down the surface, never up. That's a simplified version
# of our own "law of motion". So we can update v by:

# v = v - learning_rate * gradient(C)

# Given that, we can use a gradient to calculate values of weights and biases
# that minimizes the cost function C:

# wk = wk - learning_rate * derivative(C, wk)
# bl = bl - learning_rate * derivative(C, wl)

# If we apply that over time, our "ball" will roll down the hill of C. That's
# our "rule to learn".

# Sthocastic gradient descent: only calculates gradient for a batch/pool and
# use that to average the wk and bl.

def C(v):
    pass

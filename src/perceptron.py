class Perceptron:
    def __init__(self, w, x, threshold):
        self.w = w
        self.x = x
        self.threshold = threshold

    def run(self):
        sum_ = 0
        for j in xrange(0, len(self.w)):
            sum_ += self.w[j] * self.x[j]
        if sum_ <= self.threshold:
            return 0
        else:
            return 1

neuron = Perceptron([6.0, 2.0, 2.0], [0, 1, 0], 0.5)
print neuron.run()

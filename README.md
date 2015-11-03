# Learning Deep Learning

# Introduction to Neural Networks

## Perceptron

- Sigmoid neuron is more common than Perceptron
- Use step function as activation function
- Small changes in weights/bias produce large changes in output (which is bad for
  training, we want the network learning smoothly)

Perceptron is a device that makes decisions by weighting up evidences.

## Sigmoid neurons

- Use sigmoid function as activation function: smoother than step function
- Small changes in weights/bias produce small changes in output
- Wrong called Multi Layer Perceptrons (MLP)

## Parts of a neural network

- Input layers
- Hidden layers
- Output layers

It's really straightforward to design input and output layers.
Input can be pixels of an image, or characters of a phrase; and output can
be how much an image can be a pattern. However,
designing hidden layers is an art. There's many design heuristics that guides
the creation of such hidden layers.

We're going to use feedforward networks: networks that doesn't has loops.

There's some networks that have loops, and they're called recurrent neural
networks. RNNs have loops that fires for some time duration and after a while
they stop firing. They're commonly less powerful than feedforward networks but
simulate more closely our brains.

## Gradient descent as objective/loss function

We need an optimization function that we'll use to optimize weights and bias
during neural network training.

We can use the mean squared error (MSE) as a loss function:

```
C(w, b) = 1/2n * sum(|y(x) - a|**2)
```

n: number of inputs
y(x): derided output for input x
a: actual output of our neural network

It gives us how much our neural network output is different from the
desired/expected output. Large C reveals larger difference, larger the loss.
So, our goal is to minimize C. In other words, we need to find the best set
of weights and bias that minimizes the cost C. We will do that using an
algorithm called gradient descent.

The loss function is a sweet way to follow how a neural network is improving
over time (better than the positive/negative ratio, for example). Classification
accuracy is a second step, a complementary measurement while analyzing a
neural net, or in other words, to evaluate learning.

# References

## Books and tutorials

I'm starting with

1. http://cs231n.github.io/classification/
2. http://neuralnetworksanddeeplearning.com/

Then going to Theano tutorials and Caffe.

Starting using Theano and Caffe.

## Libraries and frameworks

Low-level to high-level:

- Caffe
- Theano
- Mozi: https://github.com/hycis/Mozi
- PyLearn2
- Keras

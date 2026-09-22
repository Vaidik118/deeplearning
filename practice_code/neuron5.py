import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    return max(0, x)


def tanh(x):
    return math.tanh(x)


numbers = [-2, -1, 0, 1, 2]

for x in numbers:
    print("x =", x)
    print("Sigmoid:", sigmoid(x))
    print("ReLU:", relu(x))
    print("Tanh:", tanh(x))
    print()
import math

# Inputs
x1 = 8
x2 = 7

# Weights
w1 = 0.6
w2 = 0.4

# Bias
b = 1

# Weighted sum
z = x1 * w1 + x2 * w2 + b

# Sigmoid activation
output = 1 / (1 + math.exp(-z))

print("Weighted sum:", z)
print("Neuron output:", output)
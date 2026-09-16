import math



x = 1
w = 0.1
b = 0
target = 1
z = x * w  + b
output = 1 / (1 + math.exp(-z))
print("Weighted sum:", z)
print("Neuron output:", output)

loss = (target - output)**2
print("Loss:", loss)
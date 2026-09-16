import math

# Training data
X = [1, 2, 3, 4, 5]
Y = [0, 0, 0, 1, 1]

# Initial parameters
w = 0.1
b = 0.0

# Learning rate
lr = 0.1


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


for epoch in range(1000):

    total_loss = 0

    for x, target in zip(X, Y):

        # Forward pass
        z = x * w + b
        prediction = sigmoid(z)

        # Loss
        loss = (target - prediction) ** 2
        total_loss += loss

        # Gradient
        dz = 2 * (prediction - target)
        dz *= prediction * (1 - prediction)

        dw = dz * x
        db = dz

        # Update
        w = w - lr * dw
        b = b - lr * db

    if epoch % 100 == 0:
        print("Epoch:", epoch,
              "Loss:", total_loss)


print("Final weight:", w)
print("Final bias:", b)

# Test
for x in X:
    prediction = sigmoid(x * w + b)
    print(x, prediction)
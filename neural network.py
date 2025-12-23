import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

inputs = [1, 0, 1]
weights = [0.5, -0.6, 0.2]
bias = 0.1

net = sum(i*w for i, w in zip(inputs, weights)) + bias
output = sigmoid(net)

print("Output:", output)

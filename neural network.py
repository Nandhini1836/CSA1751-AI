import math

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(y):
    return y * (1 - y)

# Inputs
x1 = 0.35
x2 = 0.9
target = 0.5
eta = 1  # learning rate

# Initial weights
w13 = 0.1
w23 = 0.8
w14 = 0.4
w24 = 0.6
w35 = 0.3
w45 = 0.9

print("---- FORWARD PASS ----")

# Hidden layer
a3 = w13 * x1 + w23 * x2
y3 = sigmoid(a3)

a4 = w14 * x1 + w24 * x2
y4 = sigmoid(a4)

# Output layer
a5 = w35 * y3 + w45 * y4
y5 = sigmoid(a5)

print("y3 =", round(y3, 3))
print("y4 =", round(y4, 3))
print("Output y5 =", round(y5, 3))

# Error
error = target - y5
print("Error =", round(error, 3))

print("\n---- BACKWARD PASS ----")

# Output delta
delta5 = error * sigmoid_derivative(y5)

# Hidden deltas
delta3 = sigmoid_derivative(y3) * w35 * delta5
delta4 = sigmoid_derivative(y4) * w45 * delta5

# Update weights (output layer)
w35 += eta * delta5 * y3
w45 += eta * delta5 * y4

# Update weights (hidden layer)
w13 += eta * delta3 * x1
w23 += eta * delta3 * x2
w14 += eta * delta4 * x1
w24 += eta * delta4 * x2

print("\nUpdated Weights:")
print("w13 =", round(w13, 3), "w23 =", round(w23, 3))
print("w14 =", round(w14, 3), "w24 =", round(w24, 3))
print("w35 =", round(w35, 3), "w45 =", round(w45, 3))

print("\n---- FORWARD PASS AFTER TRAINING ----")

# Forward pass again
a3 = w13 * x1 + w23 * x2
y3 = sigmoid(a3)

a4 = w14 * x1 + w24 * x2
y4 = sigmoid(a4)

a5 = w35 * y3 + w45 * y4
y5_new = sigmoid(a5)

print("New Output y5 =", round(y5_new, 3))
print("New Error =", round(target - y5_new, 3))



EXAMPLE 2


import math

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Inputs
x1, x2, x3 = 1, 0, 1

# Weights
w14, w24, w34 = 0.2, 0.4, -0.5
w15, w25, w35 = -0.3, 0.1, 0.2
w46, w56 = -0.3, -0.2

# Biases
theta4 = -0.4
theta5 = 0.2
theta6 = 0.1

# Learning rate
eta = 0.9

# Desired output
target = 1

# -------- Forward Pass --------

# Hidden layer calculations
a4 = x1*w14 + x2*w24 + x3*w34 + theta4
y4 = sigmoid(a4)

a5 = x1*w15 + x2*w25 + x3*w35 + theta5
y5 = sigmoid(a5)

# Output layer calculation
a6 = y4*w46 + y5*w56 + theta6
y6 = sigmoid(a6)

# Error
error = target - y6

# Display results
print("Hidden neuron H4 output:", round(y4, 3))
print("Hidden neuron H5 output:", round(y5, 3))
print("Output neuron O6:", round(y6, 3))
print("Error:", round(error, 3))

# -------- Weight Update (Output Layer) --------

delta6 = error * y6 * (1 - y6)

dw46 = eta * delta6 * y4
dw56 = eta * delta6 * y5

w46_new = w46 + dw46
w56_new = w56 + dw56

print("\nUpdated Weights:")
print("w46 new =", round(w46_new, 3))
print("w56 new =", round(w56_new, 3))

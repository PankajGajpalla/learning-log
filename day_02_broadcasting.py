import numpy as np

# Block 1
a = np.array([1, 2, 3])
b = 10
# Predict the shape and a value or two of (a + b):
# YOUR PREDICTION: [1,2,3]+[10,10,10] = [11,12,13] sape: 1,3
print(a + b)

# Block 2 
a = np.array([[1, 2, 3], [4, 5, 6]])     # shape (2, 3)
b = np.array([10, 20, 30])                # shape (3,)
# Predict shape and the resulting array:
# YOUR PREDICTION:[[11,22,33],[14, 25,36]] spae:2,3
print(a + b)

# Block 3
a = np.array([[1, 2, 3], [4, 5, 6]])     # shape (2, 3)
b = np.array([[10], [20]])                # shape (2, 1)
# Predict shape and result:
# YOUR PREDICTION: [[11, 12, 13], [24, 25, 26]] shape: 2,3
print(a + b)

# Block 4 — will this work?
a = np.array([[1, 2, 3], [4, 5, 6]])     # shape (2, 3)
b = np.array([10, 20])                    # shape (2,)
# Predict: does this work, or does it error? Why?
# YOUR PREDICTION: it will give error , cuase (2,3) and (1,2) the end is (3,2) not matching neither 1
try:
    print(a + b)
except Exception as e:
    print(f"Error: {e}")

# Block 5 — the trick to make Block 4 work
# Reshape b so it lines up correctly with a. Then a + b should work
# and add 10 to the first row, 20 to the second row.
# Hint: what shape should b be? (2, ?)
# YOUR CODE:
b = b.reshape(2,1)
print(a+b)
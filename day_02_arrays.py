import numpy as np

# === DIFFERENCE 1: One type per array ===
# Python lists hold anything: [1, "two", 3.0, [4]] is valid
# NumPy arrays hold ONE dtype. This is why they're fast.

arr = np.array([1,2,3,4,5])
print(f"Array: {arr}")
print(f"Shape: {arr.shape}")
print(f"Dtype: {arr.dtype}")

floats = np.array([1.0, 2.0, 3.0])
print(f"Float dtype: {floats.dtype}")

mixed = np.array([1, 2.5, 3])
print(f"Mixed: {mixed}, dtype: {mixed.dtype}")  # all become float!


# === DIFFERENCE 2: Math on arrays applies element-wise ===
# This is the heart of vectorization.

a = np.array([1,2,3,4,5])
b = np.array([10,20,30,40,50])

print(f"a + b = {a+b}")
print(f"a * b   = {a * b}")    # [10, 40, 90, 160] — element-wise, NOT matrix mult
print(f"a ** 2  = {a ** 2}")   # [1, 4, 9, 16]
print(f"a + 100 = {a + 100}")  # [101, 102, 103, 104] — broadcasting!

# === DIFFERENCE 3: Multi-dimensional arrays ===
# Lists of lists work but are awkward. NumPy treats them naturally.

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(f"matrix: {matrix}")
print(f"shape: {matrix.shape}")
print(f"dimension: {matrix.ndim}")
print(f"total elements: {matrix.size}")


# === DIFFERENCE 4: Useful creation functions ===
print(f"\nzeros:\n {np.zeros((2,3))}")
print(f"\nones:\n {np.ones((2,3))}")
print(f"\nidentity:\n {np.eye(3)}")
print(f"\na range:\n {np.arange(0,10,2)}")
print(f"\nlinsapce: \n{np.linspace(0,1,5)}")

rng = np.random.default_rng(seed=42)
print(f"\nrandom normal:\n{rng.normal(0,1, size=(2,3))}")

import numpy as np

# 1D indexing — just like lists
arr = np.array([10, 20, 30, 40, 50])
print(f"arr[0]   = {arr[0]}")     # 10  (first element)
print(f"arr[-1]  = {arr[-1]}")    # 50  (last element)
print(f"arr[1:4] = {arr[1:4]}")   # [20, 30, 40]  (slice: start inclusive, end exclusive)
print(f"arr[::2] = {arr[::2]}")   # [10, 30, 50]  (every 2nd element)
print(f"arr[::-1] = {arr[::-1]}") # [50, 40, 30, 20, 10]  (reversed)


# 2D indexing — rows first, then columns
m = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
])
# Shape: (3, 4) — 3 rows, 4 columns

print(f"m[0, 0]   = {m[0, 0]}")    # 1  (top-left)
print(f"m[1, 2]   = {m[1, 2]}")    # 7  (row 1, column 2)
print(f"m[2, -1]  = {m[2, -1]}")   # 12 (last row, last column)

# Whole rows and columns
print(f"m[0, :]   = {m[0, :]}")    # [1, 2, 3, 4]   (first row)
print(f"m[:, 0]   = {m[:, 0]}")    # [1, 5, 9]      (first column)
print(f"m[1:3, 1:3]:\n{m[1:3, 1:3]}")  # submatrix: rows 1-2, cols 1-2

data = np.array([15, 22, 12, 23, 30, 34, 29, 14])

mask = data>20
print(f"mask: {mask}")
print(f"data>20: {data[mask]}")
print(data[data>20])
print(f"Between 10 and 30: {data[(data > 10) & (data < 30)]}") 

print(data[[0,1,2]])

m = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])
print(f"First and third rows:\n{m[[0, 2]]}")
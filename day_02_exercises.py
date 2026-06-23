import numpy as np

rng = np.random.default_rng(seed=42)

rn20 = rng.integers(0,101,20)

print(rn20)

print(f"mean: {rn20.mean()}")
print(f"max: {rn20.max()}")
print(f"min: {rn20.min()}")
print(f"std: {rn20.std()}")


# Exercise 2: Create a 5x5 matrix of random floats from a normal
# distribution (mean=0, std=1). Then:
#   (a) Print the whole matrix
#   (b) Print only the diagonal (hint: np.diag)
#   (c) Print the second row
#   (d) Print the last column
#   (e) Print the 3x3 submatrix in the top-left corner
# ============================================================

m = rng.normal(loc=0.0, scale=1, size=(5,5))

print(f"matrix: \n{m}")
print(f"diagonal: \n{m.diagonal()}")
print(f"second row: \n{m[2]}")
print(f"last col: {m[:,-1]}")
print(f"3x3 matrics: {m[:3, :3]}")


# (a) How many students passed (score >= 60)?
# (b) What's the average score of those who passed?
# (c) What's the average score of those who failed?
# (d) Replace all scores below 60 with 0, leave others unchanged.
#     Hint: np.where(condition, value_if_true, value_if_false)

scores = np.array([72, 88, 45, 91, 67, 30, 85, 58, 79, 95, 22, 70])


passed = scores>=60
pass_count = passed.sum()
print(f"no. of student passed: {pass_count}")

passing_scores = scores[passed]
failing_score = scores[~passed]

print(f"avg of passed: {passing_scores.mean():.2f}")
print(f"avg of failed: {failing_score.mean():.2f}")

re_scores = np.where(scores<60, 0, scores)
print(f"re_scores: {re_scores}")



# ============================================================
# Exercise 4: STRETCH — try this, it's harder than it looks.
# Without using a loop, generate the following 5x5 matrix:
#
#  [[ 0  1  2  3  4]
#   [ 1  2  3  4  5]
#   [ 2  3  4  5  6]
#   [ 3  4  5  6  7]
#   [ 4  5  6  7  8]]
#
# Each cell is row_index + column_index.
# Hint: np.arange + reshape + broadcasting. Think about what happens
# when you add a column vector to a row vector.
# ============================================================

col = np.arange(5).reshape(1,5)
row = np.arange(5).reshape(5,1)
n_arr = row + col
print(n_arr)


raw = np.array([
    [85, 72, 91],
    [60, 88, 75],
    [78, 65, 80],
    [92, 70, 88],
    [55, 80, 70],
])

col_mean = raw.mean(axis=0)
col_std = raw.std(axis=0)

normalized_raw = (raw - col_mean)/col_std

print(f"col_mean: {col_mean}")
print(f"col_std: {col_std}")

print(normalized_raw)

print(f"mean: {normalized_raw.mean(axis=0)}")
print(f"std: {normalized_raw.std(axis=0)}")
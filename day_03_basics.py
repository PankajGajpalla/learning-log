import pandas as pd
import numpy as np

# === Series: a labeled 1D array ===
ages = pd.Series([25, 32, 47, 19], index=["Alice", "Bob", "Carol", "Dan"])
print("=== Series ===")
print(ages)
print(f"Alice's age: {ages['Alice']}")
print(f"Type: {type(ages)}")
print(f"Underlying values (a numpy array!): {ages.values}")
print(f"Mean age: {ages.mean()}")
print(f"Ages > 25: {ages[ages > 25].tolist()}")


# === DataFrame: a labeled 2D table ===
# Each column is named. Each column has its own dtype.
df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Carol", "Dan", "Eve"],
    "age":    [25, 32, 47, 19, 38],
    "city":   ["Mumbai", "Delhi", "Mumbai", "Bangalore", "Delhi"],
    "salary": [55000, 72000, 95000, 38000, 81000],
})

print("\n=== DataFrame ===")
print(df)
print(f"\nShape: {df.shape}")        # (rows, columns)
print(f"\nColumn types:\n{df.dtypes}")
print(f"\nIndex: {df.index.tolist()}")    # default index is 0..N-1
print(f"Columns: {df.columns.tolist()}")


# Summary stats for all numeric columns
print(f"\n=== describe() — your most-used method ===")
print(df.describe())

# Quick look — head shows first N rows
print(f"\n=== head(3) ===")
print(df.head(3))

# info() shows column types and missing values
print(f"\n=== info() ===")
df.info()
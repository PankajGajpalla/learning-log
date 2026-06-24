import pandas as pd

df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Carol", "Dan", "Eve", "Frank", "Grace"],
    "age":    [25, 32, 47, 19, 38, 51, 28],
    "city":   ["Mumbai", "Delhi", "Mumbai", "Bangalore", "Delhi", "Mumbai", "Bangalore"],
    "salary": [55000, 72000, 95000, 38000, 81000, 110000, 62000],
    "dept":   ["eng", "sales", "eng", "intern", "sales", "eng", "sales"],
})

# === Selecting columns ===
print("Single column (returns a Series):")
print(df["name"])

print("\nMultiple columns (returns a DataFrame — note double brackets):")
print(df[["name", "salary"]])

# === Selecting rows — two ways ===
# .loc — by label (whatever the row index is named)
# .iloc — by integer position (always 0, 1, 2, ...)

print("\n.iloc[0]  — first row by position:")
print(df.iloc[0])

print("\n.loc[0]   — row with index label 0 (same here because default index is 0..N-1):")
print(df.loc[0])

# Slicing: pay close attention
print("\n.iloc[0:3]  — rows at positions 0, 1, 2 (end EXCLUSIVE, like Python/NumPy):")
print(df.iloc[0:3])

print("\n.loc[0:3]   — rows with labels 0, 1, 2, 3 (end INCLUSIVE — this is Pandas-specific!):")
print(df.loc[0:3])


# === Selecting rows AND columns together ===
print("\nRows 1-3, columns 'name' and 'salary':")
print(df.loc[0:3, ["name", "salary"]])

print("\nBy position — first 3 rows, first 2 columns:")
print(df.iloc[0:3, 0:2])


# === Filtering with boolean masks (same as NumPy) ===
print("\nPeople over 30:")
print(df[df["age"] > 30])

print("\nEngineers earning more than 60k:")
print(df[(df["dept"] == "eng") & (df["salary"] > 60000)])

# === isin: filter by membership in a list ===
print("\nPeople in Mumbai or Bangalore:")
print(df[df["city"].isin(["Mumbai", "Bangalore"])])

# === query: a string-based alternative (sometimes cleaner) ===
print("\nUsing query — same result:")
print(df.query("city in ['Mumbai', 'Bangalore'] and age > 25"))
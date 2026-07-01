import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Always start with a copy when cleaning — never destroy the original.
clean = df.copy()

# === Step 1: Decide what to do with missing values ===
# Print missing counts again so we know what we're dealing with.
print("Missing values before cleaning:")
print(clean.isna().sum())
print()

# ----------------------------------------------------------------
# Task 1 (I'll show you): Fill missing Age with the median age.
# Why median, not mean? Median is robust to outliers. The Titanic
# has a few very old passengers; using the mean would shift our
# fill value upward. Median = "typical age", a safer default.
# ----------------------------------------------------------------
median_age = clean["Age"].median()
print(f"Median age (will be our fill value): {median_age}")
clean["Age"] = clean["Age"].fillna(median_age)

# Verify
print(f"Missing ages after fill: {clean['Age'].isna().sum()}")

# ----------------------------------------------------------------
# Task 2 (you): Embarked has 2 missing values. Fill them with the most
# common value (the "mode"). 
# Hints:
#   - clean["Embarked"].mode() returns a Series (could be multiple modes)
#   - Grab the first one with .mode()[0] or .mode().iloc[0]
# After filling, verify with isna().sum()
# ----------------------------------------------------------------

Embarked_mod = clean["Embarked"].mode()[0]
print(f"mode of Embarked: {Embarked_mod}")
clean["Embarked"] = clean["Embarked"].fillna(Embarked_mod)

print(clean["Embarked"].isna().sum())

# ----------------------------------------------------------------
# Task 3 (you): Cabin is 77% missing. Imputing is silly — instead, 
# create a new binary column "has_cabin" that is 1 if Cabin is not 
# missing, 0 otherwise. Then DROP the original Cabin column.
# 
# Hints:
#   - clean["Cabin"].notna() returns a boolean Series — but we want 1/0
#   - .astype(int) converts True/False to 1/0
#   - clean = clean.drop(columns=["Cabin"]) to drop a column
# 
# After: print clean.columns to confirm Cabin is gone and has_cabin exists.
# Also print the value_counts of has_cabin so you can see the split.
# ----------------------------------------------------------------
print("modifing Cabin column")
has_cabin = clean["Cabin"].notna().astype(int)

clean = clean.drop(columns=["Cabin"])
print(clean.columns)

print(has_cabin.value_counts())

clean["has_cabin"] = has_cabin

print(clean.columns)
print(clean.head(3))
print("modified Cabin column")



# ----------------------------------------------------------------
# Task 4 (you): Drop columns we won't use for modeling. 
# Drop: PassengerId, Name, Ticket
# Why? PassengerId is just a row number (no info). Name is text with 
# many unique values (we'd need NLP to use it). Ticket is messy strings.
# We'll keep them off the table for now.
# 
# Hint: drop multiple columns by passing a list to columns=
# ----------------------------------------------------------------

clean = clean.drop(columns=["PassengerId", "Name", "Ticket"])
print(clean.columns)

# ----------------------------------------------------------------
# Task 5 (you): Convert Sex to numeric. Models can't read "male"/"female".
# Map: "male" → 0, "female" → 1
# 
# Hint: clean["Sex"] = clean["Sex"].map({"male": 0, "female": 1})
# 
# Then print clean["Sex"].value_counts() to confirm it's now numeric.
# ----------------------------------------------------------------
# print(clean["Sex"].value_counts())
clean["Sex"] = clean["Sex"].map({"male":0, "female":1})
print(clean["Sex"].value_counts())

# ----------------------------------------------------------------
# Task 6 (you): Convert Embarked to numeric too.
# It has values "S", "C", "Q". Use one-hot encoding:
#   pd.get_dummies(clean, columns=["Embarked"], drop_first=True)
# This creates new columns Embarked_Q and Embarked_S (drops C to avoid 
# redundancy — if both Q and S are 0, it must be C).
# 
# Assign the result back to `clean`.
# Then print clean.columns and clean.head().
# ----------------------------------------------------------------
clean = pd.get_dummies(clean, columns=["Embarked"], drop_first=True, dtype=int)

print(clean.columns)
print(clean.head())


# ----------------------------------------------------------------
# Final check
# ----------------------------------------------------------------
print("\n=== FINAL ===")
print(f"Shape: {clean.shape}")
print(f"Dtypes:\n{clean.dtypes}")
print(f"Missing:\n{clean.isna().sum()}")
print(f"\nFirst 5 rows:\n{clean.head()}")

# Save the cleaned data for tomorrow.
clean.to_csv("titanic_clean.csv", index=False)
print("\nSaved to titanic_clean.csv")

# Add this near the end, before saving:
print("\n=== Spot-check Fare and Age are still floats ===")
print(f"Fare dtype: {clean['Fare'].dtype}")    # should be float64
print(f"Age dtype:  {clean['Age'].dtype}")     # should be float64
print(f"\nFirst 3 Fare values: {clean['Fare'].head(3).tolist()}")
# Should show [7.25, 71.2833, 7.925] — with decimals!

print(f"\nFirst 3 Age values: {clean['Age'].head(3).tolist()}")
# Should show [22.0, 38.0, 26.0]
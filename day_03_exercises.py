import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

print(df.head())
print(df.describe())
# ============================================================
# Exercise 1: How many men and women were on board? 577 men and 314 women
# Hint: .value_counts() on the Sex column
# ============================================================

print(f"sex counts: \n {df["Sex"].value_counts()}")

# ============================================================
# Exercise 2: What was the overall survival rate?  0.383838
# Hint: Survived is 0 or 1. The mean of a 0/1 column is the proportion of 1s.
# ============================================================
print((df["Survived"].sum())/df["Survived"].count())
# print(f"survival rate: \n {df[]}")


# ============================================================
# Exercise 3: Survival rate by sex.
# What fraction of women survived? What fraction of men survived?
# Hint: filter first, then mean — OR use .groupby("Sex")["Survived"].mean()
# Try both approaches.
# ============================================================
women_survived_rate = df[(df["Sex"]=="female") & (df["Survived"])]["Sex"].count()/(df[df["Sex"]=="female"]["Sex"].count())
print(f"women survived rate: {women_survived_rate:0.2f}")
male_survived_rate = df[(df["Sex"]=="male") & (df["Survived"])]["Sex"].count()/(df[df["Sex"]=="male"]["Sex"].count())
print(f"male survived rate: {male_survived_rate:.2f}")

print(df.groupby("Sex")["Survived"].mean())


# ============================================================
# Exercise 4: Survival rate by passenger class (Pclass: 1=first, 2=second, 3=third).
# Hint: groupby again.
# ============================================================
surival_rate_by_pclass = df.groupby("Pclass")["Survived"].mean()
print(surival_rate_by_pclass)


# ============================================================
# Exercise 5: The youngest survivor — who were they, and how old?
# Hint: filter survivors first, then find min age, then find that row.
# Print their Name and Age.
# ============================================================
youngest_surviver = (df[df["Survived"]==1]["Age"]).min()
print(df[df["Age"]==youngest_surviver][["Name","Age"]])


# ============================================================
# Exercise 6: Create a new column "age_group" with these bins:
#   - 0-12   → "child"
#   - 13-19  → "teen"
#   - 20-59  → "adult"
#   - 60+    → "senior"
# Then show the survival rate by age_group.
# 
# Hint: pd.cut(df["Age"], bins=[0, 12, 19, 59, 200], labels=["child", "teen", "adult", "senior"])
# 
# Watch out: some passengers have missing Age. That's fine — they'll just be NaN
# in age_group and won't appear in the groupby result.
# ============================================================

age_group = pd.cut(df["Age"], bins=[0, 12, 19, 59, 200], labels=["child", "teen", "adult", "senior"])

print(df.groupby(age_group)["Survived"].mean())


# ============================================================
# Exercise 7 (STRETCH): Combine class AND sex for survival.
# Hint: groupby on a LIST of columns: df.groupby(["Pclass", "Sex"])["Survived"].mean()
# Look at the result. What story does it tell?
# ============================================================

print(df.groupby(["Pclass", "Sex"])["Survived"].mean())

# it tells the Sex survival rate for different class 

survivors = df[df["Survived"] == 1]
print(survivors.nsmallest(1, "Age")[["Name", "Age"]])
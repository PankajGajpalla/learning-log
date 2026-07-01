import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("titanic_clean.csv")
y = df["Survived"]
X = df.drop(columns=["Survived"])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ============================================================
# Exercise 1: The dumb baseline
# Build a "model" that predicts EVERYONE DIES (always predicts 0).
# What's its accuracy on the test set?
# 
# Hint: y_pred_dumb = np.zeros(len(y_test)) — or np.zeros_like(y_test)
# Then use accuracy_score.
# 
# This is your floor. Any real model must beat this number.
# ============================================================


y_pred_dumb = np.zeros(len(y_test))

acc_baseline = accuracy_score(y_test, y_pred_dumb) 
print(f"accuracy: {acc_baseline:.4f}")



# ============================================================
# Exercise 2: The "women survive, men die" rule from history
# Build a simple non-ML rule: if Sex == 1 (female), predict 1, else 0.
# What's its accuracy?
# 
# Hint: y_pred_rule = (X_test["Sex"] == 1).astype(int).values
# 
# A real model with all 9 features must beat this 1-feature rule.
# Otherwise the extra features aren't earning their keep.
# ============================================================

y_pred_rule = (X_test["Sex"]==1).astype(int).values

acc_sex_only = accuracy_score(y_test, y_pred_rule)
print(f"accuracy: {acc_sex_only:.4f}")



# ============================================================
# Exercise 3: K-Nearest Neighbors classifier
# Train a KNN classifier with k=5. Report test accuracy and confusion matrix.
# 
# from sklearn.neighbors import KNeighborsClassifier
# knn = KNeighborsClassifier(n_neighbors=5)
# 
# KNN is sensitive to feature scale (it computes distances). 
# Don't fix that yet — train on raw features for now and SEE the problem.
# ============================================================
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

y_pred_knn = knn.predict(X_test)
acc_knn_raw = accuracy_score(y_test, y_pred_knn)
print(f"accuracy knn: {acc_knn_raw:.4f}")

print(confusion_matrix(y_test, y_pred_knn))


# ============================================================
# Exercise 4: Scale the features, then retrain KNN
# StandardScaler standardizes each feature to mean=0, std=1.
# We did this by hand on Day 2!
# 
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)
# 
# CRITICAL: fit_transform on TRAIN, transform only on TEST.
# Never call .fit() on test data — that's data leakage. We learn the 
# scaling parameters from train and APPLY them to test as-is.
# 
# Retrain KNN on scaled data. Report new accuracy.
# Compare to Exercise 3 — how much did scaling help?
# ============================================================

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


knn.fit(X_train_scaled,y_train)
y_pred_knn_stdsclr = knn.predict(X_test_scaled)

acc_knn_scaled = accuracy_score(y_test, y_pred_knn_stdsclr)
print(f"accuracy of scaled: {acc_knn_scaled:.4f}")

print(f"compareing unscaled and scaled : {(acc_knn_scaled - acc_knn_raw):.4f}")



# ============================================================
# Exercise 5: Compare all five models in one table
# Build a small DataFrame with model name and test accuracy for:
#   - Baseline (everyone dies)
#   - Sex-only rule
#   - Logistic Regression
#   - KNN (raw)
#   - KNN (scaled)
#   - Random Forest
# 
# Sort by accuracy descending. Print it.
# Write a one-sentence comment underneath about what the comparison tells you.
# ============================================================

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
acc_lr = accuracy_score(y_test, y_pred_lr)

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
acc_rf = accuracy_score(y_test, y_pred_rf)

data = {
    "models": ["Baseline", "Sex_only_rule", "Logistic_Regression", "KNN_raw", "KNN_scaled", "Random_Forest"],
    "acc": [acc_baseline, acc_sex_only, acc_lr, acc_knn_raw, acc_knn_scaled, acc_rf]
}
df = pd.DataFrame(data).sort_values("acc", ascending=False)

print(df)


# ============================================================
# Exercise 6 (STRETCH): Find the passenger your best model was most CONFIDENT about — and wrong.
# 
# Logistic regression and Random Forest both have a .predict_proba() method
# that returns probabilities instead of hard predictions.
# 
# For your best model:
#   1. Get probabilities for the test set
#   2. Find the passenger where the model said "I'm 95%+ sure they survived" 
#      but they actually died (or vice versa)
#   3. Print that passenger's features
# 
# Hint: probs = model.predict_proba(X_test) returns shape (n_test, 2)
#       probs[:, 1] is the probability of class 1 (survived)
#       Find rows where probs[:, 1] > 0.95 but y_test == 0
# ============================================================

# Use logistic regression — trained on unscaled X_train, so consistent with X_test
best = lr
probs = best.predict_proba(X_test)
surv_probs = probs[:, 1]

y_test_reset = y_test.reset_index(drop=True)
X_test_reset = X_test.reset_index(drop=True)

# --- Confidently wrong: predicted survived, actually died ---
died_positions = np.where(y_test_reset == 0)[0]
worst_death_pos = died_positions[np.argmax(surv_probs[died_positions])]

print(f"\n--- Model said SURVIVED, actually DIED ---")
print(f"Model's P(survived): {surv_probs[worst_death_pos]:.3f}")
print(X_test_reset.iloc[worst_death_pos])

# --- Confidently wrong: predicted died, actually survived ---
survived_positions = np.where(y_test_reset == 1)[0]
worst_survive_pos = survived_positions[np.argmin(surv_probs[survived_positions])]

print(f"\n--- Model said DIED, actually SURVIVED ---")
print(f"Model's P(survived): {surv_probs[worst_survive_pos]:.3f}")
print(X_test_reset.iloc[worst_survive_pos])


# probs = knn.predict_proba(X_test) 
# print(probs)
# print(probs.shape)
# print(prbs[:,1])
# print(probs[:,1].shape)
# print(y_test.shape)


# print((probs[:,1][y_test == 0]))
# survive_died = np.argmax(probs[:,1][y_test == 0])
# died_survive = np.argmax(probs[:,0][y_test == 1])

# print(f"predicted as most likely survived but died:\n{X_test[y_test==0].iloc[survive_died]}")
# print(f"predicted as most likely died but survived:\n{X_test[y_test==1].iloc[died_survive]}")


from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
import pickle
import os

wine = load_wine()
X, y = wine.data, wine.target

model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X, y)

os.makedirs("../model", exist_ok=True)
with open("../model/wine_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Wine model trained and saved!")
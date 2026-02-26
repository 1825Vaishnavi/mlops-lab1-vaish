# Import necessary libraries
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

if __name__ == '__main__':
    # Load the Wine dataset (different from original Iris dataset)
    wine = load_wine()
    X, y = wine.data, wine.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)

    # Train a Decision Tree classifier (different from original Random Forest)
    model = DecisionTreeClassifier(max_depth=5, random_state=7)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {acc * 100:.2f}%")

    # Save the model to a file
    joblib.dump(model, 'wine_model.pkl')

    print("Wine dataset model training was successful!")
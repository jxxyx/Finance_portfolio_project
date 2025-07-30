from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_model(X, y, model_path="model.pkl"):
    """
    Train a Random Forest model and save it.
    Handles class imbalance using class_weight='balanced'.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, model_path)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {acc:.2f}")
    return model, acc


def load_model(model_path="model.pkl"):
    """
    Load a saved model.
    """
    return joblib.load(model_path)
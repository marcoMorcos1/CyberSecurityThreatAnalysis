from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report

def train_model(X_train, y_train):
    base_model = RandomForestClassifier(n_estimators=100, random_state=42)
    multi_target_model = MultiOutputClassifier(base_model)
    multi_target_model.fit(X_train, y_train)
    return multi_target_model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print("Attack Type Prediction Report:")
    print(classification_report(y_test.iloc[:, 0], y_pred[:, 0]))
    print("Attack Source Prediction Report:")
    print(classification_report(y_test.iloc[:, 1], y_pred[:, 1]))
    return y_pred
    


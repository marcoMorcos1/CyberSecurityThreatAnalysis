import pandas as pd
from preprocess import preprocess_data
from model import train_model, evaluate_model
from sklearn.model_selection import train_test_split
from visualizations import plot_confusion_matrices, plot_feature_importances, plot_real_vs_predicted


# Load data
data = pd.read_csv('CyberSec_Threats.csv')

# Preprocess
X, y, encoders, attack_type_encoder, attack_source_encoder = preprocess_data(data)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = train_model(X_train, y_train)

# Evaluate
y_pred = evaluate_model(model, X_test, y_test)

#Visualize
plot_confusion_matrices(y_test, y_pred, attack_type_encoder, attack_source_encoder)
plot_feature_importances(model, X.columns)
plot_real_vs_predicted(y_test, y_pred, attack_type_encoder, attack_source_encoder)
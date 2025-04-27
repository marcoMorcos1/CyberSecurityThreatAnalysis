import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import pandas as pd

def plot_confusion_matrices(y_test, y_pred, attack_type_encoder, attack_source_encoder):
    fig, axs = plt.subplots(1, 2, figsize=(18, 7))

    # Attack Type
    cm_attack_type = confusion_matrix(y_test.iloc[:, 0], y_pred[:, 0])
    sns.heatmap(cm_attack_type, annot=True, fmt='d', cmap='Blues', ax=axs[0])
    axs[0].set_title('Attack Type Confusion Matrix')
    axs[0].set_xlabel('Predicted')
    axs[0].set_ylabel('Actual')
    axs[0].set_xticklabels(attack_type_encoder.classes_, rotation=45, ha='right')
    axs[0].set_yticklabels(attack_type_encoder.classes_, rotation=0)

    # Attack Source
    cm_attack_source = confusion_matrix(y_test.iloc[:, 1], y_pred[:, 1])
    sns.heatmap(cm_attack_source, annot=True, fmt='d', cmap='Greens', ax=axs[1])
    axs[1].set_title('Attack Source Confusion Matrix')
    axs[1].set_xlabel('Predicted')
    axs[1].set_ylabel('Actual')
    axs[1].set_xticklabels(attack_source_encoder.classes_, rotation=45, ha='right')
    axs[1].set_yticklabels(attack_source_encoder.classes_, rotation=0)

    plt.tight_layout()
    plt.show()

def plot_feature_importances(model, feature_names):
    importances = model.estimators_[0].feature_importances_ 
    indices = importances.argsort()[::-1]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=importances[indices], y=[feature_names[i] for i in indices])
    plt.title('Feature Importances (First Target)')
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.show()

def plot_real_vs_predicted(y_test, y_pred, attack_type_encoder, attack_source_encoder):
    attack_type_actual = attack_type_encoder.inverse_transform(y_test.iloc[:, 0])
    attack_type_pred = attack_type_encoder.inverse_transform(y_pred[:, 0])

    attack_source_actual = attack_source_encoder.inverse_transform(y_test.iloc[:, 1])
    attack_source_pred = attack_source_encoder.inverse_transform(y_pred[:, 1])

    fig, axs = plt.subplots(2, 1, figsize=(15, 12))

    # Attack Type
    df_attack_type = pd.DataFrame({'Actual': attack_type_actual, 'Predicted': attack_type_pred})
    df_attack_type['Match'] = df_attack_type['Actual'] == df_attack_type['Predicted']
    df_attack_type['Match'] = df_attack_type['Match'].map({True: 'Correct', False: 'Incorrect'})
    df_attack_type['Count'] = 1

    sns.countplot(data=df_attack_type, x='Actual', hue='Match', ax=axs[0], palette='pastel')
    axs[0].set_title('Actual vs Predicted Attack Type')
    axs[0].set_xlabel('Attack Type')
    axs[0].set_ylabel('Count')
    axs[0].tick_params(axis='x', rotation=45)

    # Attack Source
    df_attack_source = pd.DataFrame({'Actual': attack_source_actual, 'Predicted': attack_source_pred})
    df_attack_source['Match'] = df_attack_source['Actual'] == df_attack_source['Predicted']
    df_attack_source['Match'] = df_attack_source['Match'].map({True: 'Correct', False: 'Incorrect'})
    df_attack_source['Count'] = 1

    sns.countplot(data=df_attack_source, x='Actual', hue='Match', ax=axs[1], palette='muted')
    axs[1].set_title('Actual vs Predicted Attack Source')
    axs[1].set_xlabel('Attack Source')
    axs[1].set_ylabel('Count')
    axs[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()

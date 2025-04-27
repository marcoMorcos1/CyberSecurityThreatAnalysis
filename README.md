# CyberSecurityThreatAnalysis
Project Overview
This project is focused on predicting Attack Types and Attack Sources in cybersecurity incidents using machine learning. The model is trained to analyze historical attack data and make predictions about the type of attack and its source based on features like country, year, target industry, financial loss, and more.

Problem Statement
As an aspiring SOC Analyst, quickly identifying the type and source of a cyberattack is crucial for response and mitigation. This machine learning model predicts two key aspects of cyber incidents:

Attack Type: What kind of attack was executed (e.g., Phishing, Ransomware).

Attack Source: Who or what was behind the attack (e.g., Hacker Group, Nation-state).

Data
The dataset consists of cybersecurity incident data, including columns like:

Country: The country where the attack occurred.

Year: The year of the attack.

Attack Type: Type of attack (e.g., Phishing, Ransomware).

Target Industry: Industry targeted by the attack.

Financial Loss: Losses in millions due to the attack.

Number of Affected Users: Number of users impacted by the attack.

Attack Source: The origin of the attack (e.g., Hacker Group, Insider).

Security Vulnerability Type: Vulnerabilities exploited during the attack.

Defense Mechanism: Defense mechanisms employed (e.g., VPN, Firewall).

Incident Resolution Time: Time taken to resolve the incident in hours.

Approach
Data Preprocessing: Cleaned and encoded categorical features (e.g., Attack Type, Attack Source, etc.).

Modeling: Used a Random Forest Classifier wrapped in MultiOutputClassifier to predict both Attack Type and Attack Source simultaneously.

Evaluation: Model performance was evaluated using:

Confusion Matrices to visualize classification performance.

Feature Importance to understand which features are most impactful.

Accuracy Scores for both attack type and source predictions.

Key Features
Multi-output classification: Predicts both Attack Type and Attack Source.

Confusion Matrix Visualization: Analyzes model performance for both prediction outputs.

Feature Importance: Highlights which features are most influential in predicting the attack type and source.

Real vs Predicted: Bar charts to compare actual vs predicted values.

Results
Attack Type Confusion Matrix: Visual representation of model performance on Attack Type prediction.

Attack Source Confusion Matrix: Visual representation of model performance on Attack Source prediction.

Feature Importance: Analysis of which features (e.g., Country, Year) were most important in predicting attack types and sources.

Real vs Predicted Comparison: Bar charts comparing actual vs predicted values for both Attack Type and Attack Source.

Conclusion
This project demonstrates a machine learning approach to cybersecurity incident prediction. By identifying both the attack type and source, SOC Analysts can quickly assess and respond to threats, improving organizational security and response times.


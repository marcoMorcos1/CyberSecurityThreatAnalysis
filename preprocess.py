from sklearn.preprocessing import LabelEncoder

def preprocess_data(data):
    #create copy of data
    data = data.copy()

    categorical_cols = ['Country', 'Target Industry', 'Security Vulnerability Type', 'Defense Mechanism Used']
    encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        encoders[col] = le

    # Encode targets separately
    attack_type_encoder = LabelEncoder()
    attack_source_encoder = LabelEncoder()

    data['Attack Type Encoded'] = attack_type_encoder.fit_transform(data['Attack Type'])
    data['Attack Source Encoded'] = attack_source_encoder.fit_transform(data['Attack Source'])

    # Features
    X = data[['Country', 'Year', 'Target Industry', 'Financial Loss (in Million $)', 
            'Number of Affected Users', 'Security Vulnerability Type', 'Defense Mechanism Used', 'Incident Resolution Time (in Hours)']]
    
    # Targets
    y = data[['Attack Type Encoded', 'Attack Source Encoded']]

    return X, y, encoders, attack_type_encoder, attack_source_encoder

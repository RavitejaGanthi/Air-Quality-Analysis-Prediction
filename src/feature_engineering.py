import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


def encode_features(df, columns):
    """
    Encode categorical columns.
    """
    encoders = {}

    for column in columns:
        encoder = LabelEncoder()

        df[column] = encoder.fit_transform(df[column])

        encoders[column] = encoder

    return df, encoders


def scale_features(train_data, test_data):
    """
    Scale numerical features.
    """
    scaler = StandardScaler()

    train_scaled = scaler.fit_transform(train_data)

    test_scaled = scaler.transform(test_data)

    return train_scaled, test_scaled, scaler



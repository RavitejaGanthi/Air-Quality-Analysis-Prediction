import joblib

# Load trained models
regression_model = joblib.load("models/best_regression_model.pkl")
classification_model = joblib.load("models/best_classification_model.pkl")

# Load label encoders
label_encoders = joblib.load("models/label_encoders.pkl")
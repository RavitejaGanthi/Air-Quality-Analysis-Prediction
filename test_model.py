import joblib

try:
    # Load models
    regression_model = joblib.load("models/best_regression_model.pkl")
    classification_model = joblib.load("models/best_classification_model.pkl")

    # Load preprocessing objects
    scaler = joblib.load("models/scaler.pkl")
    label_encoders = joblib.load("models/label_encoders.pkl")

    print("✅ All files loaded successfully!\n")

    print("Regression Model:")
    print(type(regression_model))

    print("\nClassification Model:")
    print(type(classification_model))

    print("\nScaler:")
    print(type(scaler))

    print("\nEncoded Columns:")
    print(label_encoders.keys())

except Exception as e:
    print("❌ Error loading files:")
    print(e)
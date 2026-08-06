import joblib

encoders = joblib.load("models/label_encoders.pkl")

for column, encoder in encoders.items():
    print(f"\n{column}")
    print(encoder.classes_)
    

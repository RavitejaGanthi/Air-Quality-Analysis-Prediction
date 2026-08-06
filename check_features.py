'''import joblib

model = joblib.load("models/best_regression_model.pkl")

print("Number of features:", model.n_features_in_)

try:
    print("\nFeature Names:")
    print(model.feature_names_in_)
except AttributeError:
    print("\nThis model does not store feature names.")'''
    
    
import joblib

model = joblib.load("models/best_regression_model.pkl")

print(model.feature_names_in_) 
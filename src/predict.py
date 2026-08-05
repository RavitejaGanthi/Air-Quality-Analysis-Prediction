import joblib


def load_model(file_path):
    return joblib.load(file_path)


def predict(model, data):
    return model.predict(data)
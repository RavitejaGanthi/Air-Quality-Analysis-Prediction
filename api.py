from fastapi import FastAPI
import joblib
import pandas as pd

from src.schemas import AQIRequest

app = FastAPI(
    title="Air Quality Prediction API",
    version="1.0.0"
)

regression_model = joblib.load("models/best_regression_model.pkl")
classification_model = joblib.load("models/best_classification_model.pkl")


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/predict-aqi")
def predict_aqi(request: AQIRequest):
    data = pd.DataFrame([request.model_dump()])
    prediction = regression_model.predict(data)
    return {"Predicted_AQI": float(prediction[0])}


@app.post("/predict-bucket")
def predict_bucket(request: AQIRequest):
    data = pd.DataFrame([request.model_dump()])
    prediction = classification_model.predict(data)
    return {"Predicted_AQI_Bucket": int(prediction[0])}
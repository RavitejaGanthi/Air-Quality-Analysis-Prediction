from fastapi import FastAPI, HTTPException

from src.schemas import (
    AirQualityInput,
    AQIResponse,
    BucketResponse,
)

from src.predict import (
    predict_aqi,
    predict_bucket,
)

from src.utils import encode_input

from src.model_loader import (
    regression_model,
    classification_model,
    label_encoders,
)

app = FastAPI(
    title="Air Quality Prediction API",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Air Quality Prediction API is running successfully."
    }


@app.post("/predict-aqi", response_model=AQIResponse)
def predict_air_quality(data: AirQualityInput):

    try:

        input_data = data.model_dump()

        # Rename to match training column
        input_data["Humidity_%"] = input_data.pop("Humidity_")

        # Encode categorical columns
        input_data = encode_input(input_data)

        prediction = predict_aqi(
            regression_model,
            input_data,
        )

        return AQIResponse(
            predicted_aqi=prediction
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post("/predict-bucket", response_model=BucketResponse)
def predict_air_quality_bucket(data: AirQualityInput):

    try:

        input_data = data.model_dump()

        input_data["Humidity_%"] = input_data.pop("Humidity_")

        input_data = encode_input(input_data)

        prediction = predict_bucket(
            classification_model,
            input_data,
            label_encoders["AQI_Bucket"],
        )

        return BucketResponse(
            predicted_bucket=prediction
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
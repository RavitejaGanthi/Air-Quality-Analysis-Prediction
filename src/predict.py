import pandas as pd

FEATURE_ORDER = [
    "state",
    "city",
    "pollutant_id",
    "pollutant_min",
    "pollutant_max",
    "pollutant_avg",
    "Temperature_C",
    "Humidity_%",
    "Wind_Speed_kmh",
]


def predict_aqi(model, input_data):

    input_df = pd.DataFrame([input_data])

    input_df = input_df[FEATURE_ORDER]

    print("\nPrediction Data")
    print(input_df)

    prediction = model.predict(input_df)

    return float(prediction[0])


def predict_bucket(model, input_data, bucket_encoder):

    input_df = pd.DataFrame([input_data])

    input_df = input_df[FEATURE_ORDER]

    prediction = model.predict(input_df)

    return bucket_encoder.inverse_transform(prediction)[0]
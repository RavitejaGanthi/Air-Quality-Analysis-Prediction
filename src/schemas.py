from pydantic import BaseModel


class AirQualityInput(BaseModel):
    state: str
    city: str
    pollutant_id: str

    pollutant_min: float
    pollutant_max: float
    pollutant_avg: float

    Temperature_C: float
    Humidity_: float
    Wind_Speed_kmh: float


class AQIResponse(BaseModel):
    predicted_aqi: float


class BucketResponse(BaseModel):
    predicted_bucket: str
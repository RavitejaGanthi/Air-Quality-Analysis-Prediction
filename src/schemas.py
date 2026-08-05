from pydantic import BaseModel


class AQIRequest(BaseModel):
    state: int
    city: int
    pollutant_id: int
    pollutant_min: float
    pollutant_max: float
    pollutant_avg: float
    Temperature_C: float
    Humidity_: float
    Wind_Speed_kmh: float
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Air Quality Analysis & Prediction",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Air Quality Analysis & Prediction System")

st.markdown("Predict **AQI** and **AQI Bucket** using Machine Learning.")

st.divider()

st.subheader("Enter Air Quality Details")

col1, col2 = st.columns(2)

with col1:
    state = st.text_input("State", "Telangana")
    city = st.text_input("City", "Hyderabad")
    pollutant = st.selectbox(
        "Pollutant",
        ["CO", "NH3", "NO2", "OZONE", "PM10", "PM2.5", "SO2"]
    )

    pollutant_min = st.number_input(
        "Pollutant Min",
        value=45.0
    )

    pollutant_max = st.number_input(
        "Pollutant Max",
        value=90.0
    )

with col2:
    pollutant_avg = st.number_input(
        "Pollutant Average",
        value=65.0
    )

    temperature = st.number_input(
        "Temperature (°C)",
        value=30.0
    )

    humidity = st.number_input(
        "Humidity (%)",
        value=60.0
    )

    wind_speed = st.number_input(
        "Wind Speed (km/h)",
        value=12.0
    )

payload = {
    "state": state,
    "city": city,
    "pollutant_id": pollutant,
    "pollutant_min": pollutant_min,
    "pollutant_max": pollutant_max,
    "pollutant_avg": pollutant_avg,
    "Temperature_C": temperature,
    "Humidity_": humidity,
    "Wind_Speed_kmh": wind_speed,
}

col1, col2 = st.columns(2)

with col1:

    if st.button("Predict AQI"):

        response = requests.post(
            f"{API_URL}/predict-aqi",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()

            st.success(
                f"Predicted AQI : {result['predicted_aqi']:.2f}"
            )
        else:
            st.error(response.text)

with col2:

    if st.button("Predict AQI Bucket"):

        response = requests.post(
            f"{API_URL}/predict-bucket",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()

            st.success(
                f"Predicted Bucket : {result['predicted_bucket']}"
            )
        else:
            st.error(response.text)
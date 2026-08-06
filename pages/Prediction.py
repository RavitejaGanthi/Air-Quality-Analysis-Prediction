import streamlit as st
import pandas as pd
import requests

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="AQI Prediction", page_icon="🤖")

st.title("🤖 Air Quality Prediction")

st.markdown("Predict **AQI** and **AQI Bucket** using the trained Machine Learning models.")

# -----------------------------
# FastAPI URL
# -----------------------------
API_URL = "http://127.0.0.1:8000"

# -----------------------------
# Load Dataset
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/air_quality_clean.csv")

df = load_data()

# -----------------------------
# Dropdown Data
# -----------------------------
states = sorted(df["state"].dropna().unique())

selected_state = st.selectbox(
    "Select State",
    states
)

cities = sorted(
    df[df["state"] == selected_state]["city"].dropna().unique()
)

selected_city = st.selectbox(
    "Select City",
    cities
)

pollutants = sorted(df["pollutant_id"].dropna().unique())

selected_pollutant = st.selectbox(
    "Select Pollutant",
    pollutants
)

# -----------------------------
# Numeric Inputs
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    pollutant_min = st.number_input(
        "Pollutant Minimum",
        min_value=0.0,
        value=20.0
    )

    pollutant_max = st.number_input(
        "Pollutant Maximum",
        min_value=0.0,
        value=80.0
    )

    temperature = st.number_input(
        "Temperature (°C)",
        value=30.0
    )

with col2:

    pollutant_avg = st.number_input(
        "Pollutant Average",
        min_value=0.0,
        value=50.0
    )

    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0
    )

    wind_speed = st.number_input(
        "Wind Speed (km/h)",
        min_value=0.0,
        value=12.0
    )

# -----------------------------
# Payload
# -----------------------------
payload = {
    "state": selected_state,
    "city": selected_city,
    "pollutant_id": selected_pollutant,
    "pollutant_min": pollutant_min,
    "pollutant_max": pollutant_max,
    "pollutant_avg": pollutant_avg,
    "Temperature_C": temperature,
    "Humidity_": humidity,
    "Wind_Speed_kmh": wind_speed,
}

st.divider()

col1, col2 = st.columns(2)

# -----------------------------
# AQI Prediction
# -----------------------------
with col1:

    if st.button("Predict AQI", use_container_width=True):

        try:

            response = requests.post(
                f"{API_URL}/predict-aqi",
                json=payload,
                timeout=10
            )

            response.raise_for_status()

            prediction = response.json()

            st.success(
                f"Predicted AQI: {prediction['predicted_aqi']:.2f}"
            )

        except requests.exceptions.ConnectionError:
            st.error("❌ FastAPI server is not running.")

        except Exception as e:
            st.error(str(e))

# -----------------------------
# AQI Bucket Prediction
# -----------------------------
with col2:

    if st.button("Predict AQI Bucket", use_container_width=True):

        try:

            response = requests.post(
                f"{API_URL}/predict-bucket",
                json=payload,
                timeout=10
            )

            response.raise_for_status()

            prediction = response.json()

            st.success(
                f"Predicted AQI Bucket: {prediction['predicted_bucket']}"
            )

        except requests.exceptions.ConnectionError:
            st.error("❌ FastAPI server is not running.")

        except Exception as e:
            st.error(str(e))
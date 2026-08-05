import streamlit as st
import pandas as pd
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Air Quality Analysis & Prediction",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Air Quality Analysis & Prediction System")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Data Analysis",
        "📈 Visualizations",
        "🤖 AQI Prediction",
        "🚦 AQI Bucket Prediction",
        "ℹ️ About"
    ]
)

if page == "🏠 Home":

    st.header("Project Overview")

    st.write("""
    This project predicts Air Quality Index (AQI)
    using Machine Learning models trained on
    historical air quality data.
    """)

    st.subheader("Technology Stack")

    st.write("""
    - Python
    - Pandas
    - Scikit-learn
    - FastAPI
    - Streamlit
    """)
    
elif page == "📊 Data Analysis":

    df = pd.read_csv("data/air_quality_clean.csv")

    st.header("Dataset Preview")

    st.dataframe(df.head())

    st.subheader("Shape")

    st.write(df.shape)

    st.subheader("Summary Statistics")

    st.dataframe(df.describe())
    
    

elif page == "📈 Visualizations":

    st.header("Visualizations")

    st.image("images/aqi_distribution.png")

    st.image("images/state_aqi.png")

    st.image("images/top_polluted_states.png")

    st.image("images/top_polluted_cities.png")

    st.image("images/correlation_heatmap.png")
    

elif page == "🤖 AQI Prediction":

    st.header("Predict AQI")

    state = st.number_input("State Encoding", 0)

    city = st.number_input("City Encoding", 0)

    pollutant = st.number_input("Pollutant Encoding", 0)

    pollutant_min = st.number_input("Pollutant Min")

    pollutant_max = st.number_input("Pollutant Max")

    pollutant_avg = st.number_input("Pollutant Average")

    temperature = st.number_input("Temperature")

    humidity = st.number_input("Humidity")

    wind = st.number_input("Wind Speed")

    if st.button("Predict AQI"):

        payload = {

            "state": state,

            "city": city,

            "pollutant_id": pollutant,

            "pollutant_min": pollutant_min,

            "pollutant_max": pollutant_max,

            "pollutant_avg": pollutant_avg,

            "Temperature_C": temperature,

            "Humidity_": humidity,

            "Wind_Speed_kmh": wind
        }

        response = requests.post(
            API_URL + "/predict-aqi",
            json=payload
        )

        prediction = response.json()

        st.success(
            f"Predicted AQI : {prediction['Predicted_AQI']:.2f}"
        )

elif page == "🚦 AQI Bucket Prediction":

    st.header("Predict AQI Bucket")

    state = st.number_input("State Encoding", 0)

    city = st.number_input("City Encoding", 0)

    pollutant = st.number_input("Pollutant Encoding", 0)

    pollutant_min = st.number_input("Pollutant Min")

    pollutant_max = st.number_input("Pollutant Max")

    pollutant_avg = st.number_input("Pollutant Average")

    temperature = st.number_input("Temperature")

    humidity = st.number_input("Humidity")

    wind = st.number_input("Wind Speed")

    if st.button("Predict AQI Bucket"):

        payload = {

            "state": state,

            "city": city,

            "pollutant_id": pollutant,

            "pollutant_min": pollutant_min,

            "pollutant_max": pollutant_max,

            "pollutant_avg": pollutant_avg,

            "Temperature_C": temperature,

            "Humidity_": humidity,

            "Wind_Speed_kmh": wind
        }

        response = requests.post(
            API_URL + "/predict-bucket",
            json=payload
        )

        prediction = response.json()

        st.success(
            f"Predicted AQI Bucket : {prediction['Predicted_AQI_Bucket']}"
        )
elif page == "ℹ️ About":

    st.header("About")

    st.write("""
    ## Air Quality Analysis & Prediction

    This project analyzes air quality data and
    predicts:

    - AQI
    - AQI Bucket

    ### Algorithms

    - Linear Regression
    - Decision Tree
    - Random Forest
    - Logistic Regression

    ### Developed By

    Ravi Teja
    """)
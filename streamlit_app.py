import streamlit as st

st.set_page_config(
    page_title="Air Quality Analysis & Prediction",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
    
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
.main-title{
    font-size:60px;
    font-weight:700;
    color:#2E86C1;
    text-align:center;
}


.sub-title{
    font-size:50px;
    color:#666666;
    text-align:center;
}

.card{
    background-color:#f8f9fa;
    padding:20px;
    border-radius:12px;
    box-shadow:2px 2px 10px rgba(0,0,0,0.1);
}

.footer{
    text-align:center;
    color:gray;
    margin-top:30px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------

st.markdown(
    '<p class="main-title">🌍 Air Quality Analysis & Prediction System</p>',
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="sub-title">Machine Learning • FastAPI • Streamlit</p>',
    unsafe_allow_html=True,
)

st.divider()

# ---------- Overview ----------

col1, col2 = st.columns([2, 1])

with col1:

    st.markdown("## 📌 Project Overview")

    st.write("""
This project analyzes air quality data collected across India and predicts:

- 🌫 Air Quality Index (AQI)
- 🚦 AQI Category (AQI Bucket)

using Machine Learning models built with **Scikit-learn**, served through **FastAPI**, and presented using **Streamlit**.
""")

with col2:

    st.info("""
### 📊 Dataset

✔ Indian Air Quality Dataset

✔ Weather Features

✔ Pollutant Information

✔ AQI Values

✔ AQI Categories
""")

st.divider()

# ---------- Features ----------

st.subheader("✨ Key Features")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("""
### 📊 Analysis

- Dataset Preview

- Missing Values

- Summary Statistics

- Data Quality
""")

with c2:
    st.success("""
### 📈 Visualization

- AQI Distribution

- State-wise AQI

- Top Polluted Cities

- Correlation Heatmap
""")

with c3:
    st.success("""
### 🤖 Prediction

- AQI Prediction

- AQI Bucket Prediction

- FastAPI Integration
""")

st.divider()

# ---------- Technology ----------

st.subheader("🛠 Technology Stack")

t1, t2, t3, t4 = st.columns(4)

t1.metric("Language", "Python")
t2.metric("ML", "Scikit-Learn")
t3.metric("Backend", "FastAPI")
t4.metric("Frontend", "Streamlit")

st.divider()

# ---------- Workflow ----------

st.subheader("⚙ Project Workflow")

st.code("""
Dataset
    │
    ▼
Data Cleaning
    │
    ▼
EDA
    │
    ▼
Feature Engineering
    │
    ▼
Machine Learning
    │
    ▼
FastAPI API
    │
    ▼
Streamlit Dashboard
""")

st.divider()

st.success("👈 Use the sidebar to navigate through the application.")

st.markdown(
    '<p class="footer">Developed by Raviteja Ganthi</p>',
    unsafe_allow_html=True,
)

import pandas as pd

df = pd.read_csv("data/air_quality_clean.csv")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Records", len(df))
c2.metric("States", df["state"].nunique())
c3.metric("Cities", df["city"].nunique())
c4.metric("Pollutants", df["pollutant_id"].nunique())
import streamlit as st
import pandas as pd


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Air Quality Analysis & Prediction",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main page */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Main Title */
    .main-title {
        font-size: 64px !important;
        font-weight: 800 !important;
        text-align: center !important;
        color: #2E86C1 !important;
        line-height: 1.15 !important;
        margin-top: 10px !important;
        margin-bottom: 10px !important;
    }

    /* Subtitle */
    .sub-title {
        font-size: 24px !important;
        text-align: center !important;
        color: #555555 !important;
        margin-bottom: 25px !important;
    }

    /* Cards */
    .info-card {
        background-color: #F4F8FC;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #E1E8EF;
        min-height: 180px;
    }

    .info-card h3 {
        color: #21618C;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #777777;
        padding-top: 25px;
        padding-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv("data/air_quality_clean.csv")


try:
    df = load_data()
except Exception:
    df = None


# ============================================================
# TITLE
# ============================================================

st.markdown(
    """
    <div class="main-title">
        🌍 Air Quality Analysis & Prediction System
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sub-title">
        Machine Learning • FastAPI • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# PROJECT OVERVIEW
# ============================================================

col1, col2 = st.columns([2, 1])

with col1:

    st.markdown("## 📌 Project Overview")

    st.write(
        """
        This project analyzes air quality data collected across India
        and uses Machine Learning models to predict:

        - 🌫️ **Air Quality Index (AQI)**
        - 🚦 **AQI Category (AQI Bucket)**

        The application uses **Scikit-learn** for Machine Learning,
        **FastAPI** for REST APIs, and **Streamlit** for the interactive
        web dashboard.
        """
    )


with col2:

    st.markdown(
        """
        <div class="info-card">

        <h3>📊 Dataset</h3>

        <p>✓ Indian Air Quality Dataset</p>
        <p>✓ Weather Features</p>
        <p>✓ Pollutant Information</p>
        <p>✓ AQI Values</p>
        <p>✓ AQI Categories</p>

        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


# ============================================================
# DATASET KPIs
# ============================================================

st.subheader("📊 Dataset Overview")

if df is not None:

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Records",
            f"{len(df):,}"
        )

    with col2:
        st.metric(
            "States",
            df["state"].nunique()
        )

    with col3:
        st.metric(
            "Cities",
            df["city"].nunique()
        )

    with col4:
        st.metric(
            "Pollutants",
            df["pollutant_id"].nunique()
        )

else:

    st.warning(
        "Dataset could not be loaded. "
        "Make sure data/air_quality_clean.csv exists."
    )


st.divider()


# ============================================================
# KEY FEATURES
# ============================================================

st.subheader("✨ Key Features")

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        """
        <div class="info-card">

        <h3>📊 Data Analysis</h3>

        <p>• Dataset Preview</p>
        <p>• Missing Values</p>
        <p>• Summary Statistics</p>
        <p>• Data Quality Analysis</p>

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
        <div class="info-card">

        <h3>📈 Visualization</h3>

        <p>• AQI Distribution</p>
        <p>• State-wise AQI</p>
        <p>• Top Polluted Cities</p>
        <p>• Correlation Heatmap</p>

        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
        <div class="info-card">

        <h3>🤖 Prediction</h3>

        <p>• AQI Prediction</p>
        <p>• AQI Bucket Prediction</p>
        <p>• FastAPI Integration</p>
        <p>• Real-time Predictions</p>

        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


# ============================================================
# TECHNOLOGY STACK
# ============================================================

st.subheader("🛠️ Technology Stack")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Language", "Python")

with col2:
    st.metric("Data", "Pandas")

with col3:
    st.metric("ML", "Scikit-learn")

with col4:
    st.metric("Backend", "FastAPI")

with col5:
    st.metric("Frontend", "Streamlit")


st.divider()


# ============================================================
# PROJECT WORKFLOW
# ============================================================

st.subheader("⚙️ Project Workflow")

st.code(
    """
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Exploratory Data Analysis
   │
   ▼
Feature Engineering
   │
   ▼
Machine Learning
   │
   ▼
Model Evaluation
   │
   ▼
FastAPI REST API
   │
   ▼
Streamlit Dashboard
   │
   ▼
AQI Prediction
    """,
    language="text"
)


st.divider()


# ============================================================
# MACHINE LEARNING
# ============================================================

st.subheader("🤖 Machine Learning Models")

col1, col2 = st.columns(2)


with col1:

    st.markdown(
        """
        ### Regression

        Used to predict the numerical **AQI value**.

        - Linear Regression
        - Decision Tree Regressor
        - Random Forest Regressor

        **Evaluation:**
        MAE, RMSE, R² Score
        """
    )


with col2:

    st.markdown(
        """
        ### Classification

        Used to predict the **AQI Bucket**.

        - Logistic Regression
        - Decision Tree Classifier
        - Random Forest Classifier

        **Evaluation:**
        Accuracy, Precision, Recall, F1 Score
        """
    )


st.divider()


# ============================================================
# HOW TO USE
# ============================================================

st.subheader("🚀 How to Use")

st.info(
    """
    Use the **sidebar** to navigate through the application.

    **📊 Data Analysis** → Explore the dataset

    **📈 Visualizations** → Analyze pollution trends

    **🤖 Prediction** → Predict AQI and AQI category

    **ℹ️ About** → Learn more about the project
    """
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        <hr>
        <p>
            Air Quality Analysis & Prediction System
        </p>
        <p>
            Built with Python • Scikit-learn • FastAPI • Streamlit
        </p>
        <p>
            Developed by <b>Raviteja Ganthi</b>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
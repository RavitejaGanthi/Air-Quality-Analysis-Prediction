# 🌍 Air Quality Analysis & Prediction System

A Machine Learning-powered web application that analyzes air quality data and predicts the **Air Quality Index (AQI)** and **AQI Bucket** using **Scikit-learn**, **FastAPI**, and **Streamlit**.

---

## 📌 Project Overview

This project performs:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Model Training
- AQI Prediction
- AQI Bucket Prediction
- REST API using FastAPI
- Interactive Dashboard using Streamlit

---

## 🚀 Features

- 📊 Data Analysis Dashboard
- 📈 Interactive Visualizations
- 🤖 AQI Prediction
- 🚦 AQI Bucket Prediction
- ⚡ FastAPI Backend
- 🎨 Streamlit Frontend

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Machine Learning | Scikit-learn |
| Backend | FastAPI |
| Frontend | Streamlit |
| Model Storage | Joblib |

---

## 📂 Project Structure

```text
Air-Quality-Analysis-Prediction/
│
├── data/
├── models/
├── notebooks/
├── pages/
│   ├── Home.py
│   ├── Data_Analysis.py
│   ├── Visualizations.py
│   ├── Prediction.py
│   └── About.py
│
├── src/
├── api.py
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/RavitejaGanthi/Air-Quality-Analysis-Prediction.git
```

```bash
cd Air-Quality-Analysis-Prediction
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run FastAPI

```bash
uvicorn api:app --reload
```

Swagger API:

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Streamlit

```bash
streamlit run streamlit_app.py
```

---

## 📊 Machine Learning Models

### Regression

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

### Classification

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

---

## 📈 Visualizations

- AQI Distribution
- AQI Bucket Distribution
- State-wise AQI
- City-wise AQI
- Top Polluted States
- Top Polluted Cities
- Correlation Heatmap
- Temperature vs AQI
- Humidity vs AQI
- Wind Speed vs AQI

---

## 🤖 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | API Status |
| POST | /predict-aqi | Predict AQI |
| POST | /predict-bucket | Predict AQI Bucket |

---



## 🔮 Future Improvements

- Interactive India Map
- Live AQI Data Integration
- Model Performance Dashboard
- Docker Deployment
- Cloud Deployment

---

## 👨‍💻 Author

**Raviteja Ganthi**


---

## 📄 License

This project is licensed under the MIT License.

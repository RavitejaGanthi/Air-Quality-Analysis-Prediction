import streamlit as st
import pandas as pd

st.title("📊 Data Analysis")

df = pd.read_csv("data/air_quality_clean.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Shape")

col1, col2 = st.columns(2)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])

st.subheader("Column Names")

st.write(df.columns.tolist())

st.subheader("Data Types")

st.dataframe(df.dtypes.astype(str).reset_index().rename(
    columns={"index": "Column", 0: "Data Type"}
))

st.subheader("Missing Values")

missing = df.isnull().sum().reset_index()
missing.columns = ["Column", "Missing Values"]

st.dataframe(missing)

st.subheader("Duplicate Rows")

st.metric("Duplicates", df.duplicated().sum())

st.subheader("Summary Statistics")

st.dataframe(df.describe())
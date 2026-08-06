import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📈 Air Quality Visualizations")

# Load dataset
df = pd.read_csv("data/air_quality_clean.csv")

st.subheader("AQI Distribution")

fig = px.histogram(
    df,
    x="AQI",
    nbins=40,
    title="Distribution of AQI",
)

st.plotly_chart(fig, use_container_width=True)

st.info("""
**Insight**

Most AQI values are concentrated in the lower and moderate ranges,
while fewer observations fall into very high AQI levels.
""")

st.subheader("AQI Bucket Distribution")

bucket = df["AQI_Bucket"].value_counts().reset_index()

bucket.columns = ["AQI Bucket", "Count"]

fig = px.bar(
    bucket,
    x="AQI Bucket",
    y="Count",
    color="AQI Bucket"
)

st.plotly_chart(fig, use_container_width=True)

st.info("""
**Insight**

This chart shows how frequently each air quality category occurs.
""")

st.subheader("Average AQI by State")

state = (
    df.groupby("state")["AQI"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig = px.bar(
    state,
    x="state",
    y="AQI",
    color="AQI",
)

st.plotly_chart(fig, use_container_width=True)

st.info("""
**Insight**

States with higher average AQI require greater attention to pollution control.
""")

st.subheader("Top 10 Polluted States")

top_states = state.head(10)

fig = px.bar(
    top_states,
    x="state",
    y="AQI",
    color="AQI",
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Top 10 Polluted Cities")

city = (
    df.groupby("city")["AQI"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    city,
    x="city",
    y="AQI",
    color="AQI",
)

st.plotly_chart(fig, use_container_width=True)

st.info("""
**Insight**

These cities have the highest average AQI in the dataset.
""")

st.subheader("Temperature vs AQI")

fig = px.scatter(
    df,
    x="Temperature_C",
    y="AQI",
    color="AQI"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Humidity vs AQI")

fig = px.scatter(
    df,
    x="Humidity_%",
    y="AQI",
    color="AQI"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Wind Speed vs AQI")

fig = px.scatter(
    df,
    x="Wind_Speed_kmh",
    y="AQI",
    color="AQI"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Correlation Heatmap")

numeric_df = df.select_dtypes(include="number")

fig, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    ax=ax,
)

st.pyplot(fig)

st.info("""
**Insight**

Features with stronger positive or negative correlations may have a greater influence on AQI prediction.
""")


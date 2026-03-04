import json
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Weather Dashboard")
st.title("Weather Dashboard")

rows = []
with open("weather_data.json","r") as f:
    for line in f:
        rows.append(json.loads(line))

df = pd.DataFrame(rows)
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")
filtered = df[df["city"] == "Kuala Lumpur"]
df

# KPI cards
c1, c2, c3 = st.columns(3)
c1.metric("Latest Temp (°C)", df["temperature"].iloc[-1])
c2.metric("Latest Humidity (%)", df["humidity"].iloc[-1])
c3.metric("Latest Feels Like (°C)", df["feels_like"].iloc[-1])

fig_temp = px.line(df, x="timestamp",  y="temperature", title="Temperature Over Time")
fig_humidity = px.line(filtered, x="timestamp", y="humidity", title="Humidity Over Time")
st.plotly_chart(fig_temp, use_container_width=True)
st.plotly_chart(fig_humidity, use_container_width=True)

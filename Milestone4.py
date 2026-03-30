import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.set_page_config(page_title="Demand Forecast Dashboard", layout="wide")
st.title(" XGBoost Forecast Dashboard")

# Load data
data = pd.read_csv("forecast_output.csv")

# Convert timestamp to datetime
data['timestamp'] = pd.to_datetime(data['timestamp'])

# ---- KPI CARDS ----
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Forecast", int(data['forecast'].sum()))
col2.metric("Max Demand", int(data['forecast'].max()))
col3.metric("Total Usage", int(data['units_used'].sum()))
col4.metric("Average Usage", int(data['units_used'].mean()))

# ---- LINE CHART
st.subheader(" XGBoost Prediction vs Actual")

fig, ax = plt.subplots()
ax.plot(data['timestamp'], data['units_used'], label="Actual", linestyle='--')
ax.plot(data['timestamp'], data['forecast'], label="Forecast", linewidth=2)

ax.set_xlabel("Time")
ax.set_ylabel("Usage")
ax.legend()

st.pyplot(fig)

#REGION BAR CHART
st.subheader(" Region-wise Forecast")

region_data = data.groupby('region')['forecast'].sum()

st.bar_chart(region_data)

# SERVICE TYPE PIE CHART 
st.subheader("Service Distribution")

import matplotlib.pyplot as plt

# Group data
service_data = data.groupby('service_type')['forecast'].sum().sort_values(ascending=False)

# Take top 5 and group rest as "Others"
top_n = 5
top_services = service_data[:top_n]
others = service_data[top_n:].sum()

# Add "Others"
final_data = top_services.copy()
if others > 0:
    final_data["Others"] = others

# Plot
fig, ax = plt.subplots(figsize=(7,7))

wedges, texts, autotexts = ax.pie(
    final_data,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'edgecolor': 'black'}  # clear separation
)

# Use legend instead of labels
ax.legend(wedges, final_data.index, title="Service Type",
          loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

ax.set_title("Service Type Share")

st.pyplot(fig)
#Forecast over time
st.subheader(" Daily Forecast Trend")
st.line_chart(data.set_index('timestamp')['forecast'])
#Actual vs Forecast Difference
data['difference'] = data['units_used'] - data['forecast']

st.subheader(" Prediction Error (Actual - Forecast)")
st.line_chart(data.set_index('timestamp')['difference'])

#Top Regions 
st.subheader(" Top Regions by Usage")
top_regions = data.groupby('region')['units_used'].sum().sort_values(ascending=False)
st.bar_chart(top_regions)

#Service Type vs Usage
st.subheader("⚙️ Service Type vs Usage")
st.bar_chart(data.groupby('service_type')['units_used'].sum())

#Scatter flowchart
st.subheader(" Actual vs Forecast Scatter")

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter(data['units_used'], data['forecast'])
ax.set_xlabel("Actual")
ax.set_ylabel("Forecast")

st.pyplot(fig)

st.subheader(" Usage Distribution")

fig, ax = plt.subplots()
ax.hist(data['units_used'], bins=20)

st.pyplot(fig)

#Area chart
st.subheader(" Forecast Area Chart")

st.area_chart(data.set_index('timestamp')['forecast'])
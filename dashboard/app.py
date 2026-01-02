import os
import pandas as pd
import streamlit as st

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Marketing Campaign Analysis Dashboard",
    layout="wide"
)

# --------------------------------------------------
# Load Data (SAFE PATH)
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "final_marketing_data.csv")

if not os.path.exists(DATA_PATH):
    st.error("❌ final_marketing_data.csv not found inside dashboard folder")
    st.stop()

df = pd.read_csv(DATA_PATH)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("📊 Marketing Campaign Analysis Dashboard")
st.markdown("Rule-based customer segmentation and campaign insights")

# --------------------------------------------------
# Segment Selector
# --------------------------------------------------
segment = st.selectbox(
    "Select Customer Segment",
    [
        "All",
        "High Spender",
        "High Income",
        "Family Customer",
        "Young Customer",
        "Campaign Responder",
        "High Web Engagement"
    ]
)

# --------------------------------------------------
# Filter Data Based on Segment
# --------------------------------------------------
filtered_df = df.copy()

if segment == "High Spender":
    filtered_df = df[df["High_Spender"] == 1]

elif segment == "High Income":
    filtered_df = df[df["High_Income"] == 1]

elif segment == "Family Customer":
    filtered_df = df[df["Family_Customer"] == 1]

elif segment == "Young Customer":
    filtered_df = df[df["Young_Customer"] == 1]

elif segment == "Campaign Responder":
    filtered_df = df[df["Campaign_Responder"] == 1]

elif segment == "High Web Engagement":
    filtered_df = df[df["High_Web_Engagement"] == 1]

# --------------------------------------------------
# KPI Section
# --------------------------------------------------
st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Avg Income",
    f"₹{int(filtered_df['Income'].mean())}"
)

col2.metric(
    "Avg Total Spend",
    f"₹{int(filtered_df['Total_Spend'].mean())}"
)

col3.metric(
    "Avg Web Visits / Month",
    f"{round(filtered_df['NumWebVisitsMonth'].mean(), 2)}"
)

col4.metric(
    "Campaign Response Rate",
    f"{round(filtered_df['Response'].mean() * 100, 2)}%"
)

# --------------------------------------------------
# Segment Summary
# --------------------------------------------------
st.divider()
st.subheader("📈 Segment Summary")

summary_df = filtered_df.agg({
    "Income": "mean",
    "Total_Spend": "mean",
    "Total_Purchases": "mean",
    "NumWebVisitsMonth": "mean",
    "Response": "mean"
}).to_frame(name="Average Value")

summary_df["Average Value"] = summary_df["Average Value"].round(2)

st.dataframe(summary_df)

# --------------------------------------------------
# Customer Data Preview
# --------------------------------------------------
st.divider()
st.subheader("🧾 Customer Records (Preview)")
st.dataframe(filtered_df.head(50))

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption("Marketing Campaign Analysis | Rule-Based Segmentation | Streamlit Dashboard")

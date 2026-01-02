import os
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Marketing Campaign Dashboard", layout="wide")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "final_marketing_data.csv")

df = pd.read_csv(DATA_PATH)

st.success("✅ Data loaded successfully")

# KPI Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Avg Income", f"₹{int(df['Income'].mean())}")
col2.metric("Avg Spend", f"₹{int(df['Total_Spend'].mean())}")
col3.metric("Campaign Response Rate", f"{round(df['Response'].mean()*100,2)}%")

st.divider()

# Segment Filter
segment = st.selectbox(
    "Select Segment",
    ["All","High Spender","High Income","Family Customer"]
)

if segment == "High Spender":
    df = df[df["High_Spender"] == 1]
elif segment == "High Income":
    df = df[df["High_Income"] == 1]
elif segment == "Family Customer":
    df = df[df["Family_Customer"] == 1]

st.subheader("Customer Overview")
st.dataframe(df.head(50))

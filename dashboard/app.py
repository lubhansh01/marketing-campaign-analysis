import streamlit as st
import pandas as pd

st.set_page_config(page_title="Marketing Campaign Dashboard", layout="wide")

df = pd.read_csv("../final_marketing_data.csv")

st.title("📊 Marketing Campaign Analysis")

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

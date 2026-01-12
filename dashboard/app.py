import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Marketing Campaign Analysis Dashboard",
    layout="wide"
)

# --------------------------------------------------
# Helper functions
# --------------------------------------------------
def safe_int(value):
    if pd.isna(value):
        return "N/A"
    return int(value)

def safe_percent(value):
    if pd.isna(value):
        return "N/A"
    return f"{round(value * 100, 2)}%"

# --------------------------------------------------
# Load Data (CSV inside dashboard/)
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "final_marketing_data.csv")

if not os.path.exists(DATA_PATH):
    st.error("❌ final_marketing_data.csv not found inside dashboard folder")
    st.stop()

df = pd.read_csv(DATA_PATH)

# --------------------------------------------------
# Title & Description
# --------------------------------------------------
st.title("📊 Marketing Campaign Analysis Dashboard")
st.markdown(
    """
    Interactive dashboard with **rule-based customer segmentation**
    and **dynamic data visualizations**.
    """
)

# --------------------------------------------------
# Filters (Segment + Chart Type)
# --------------------------------------------------
col_filter1, col_filter2 = st.columns(2)

with col_filter1:
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

with col_filter2:
    chart_type = st.selectbox(
        "Select Chart Type",
        [
            "Bar Chart",
            "Pie Chart",
            "Donut Chart",
            "Box Plot",
            "Histogram"
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

if filtered_df.empty:
    st.warning("⚠️ No data available for the selected segment.")
else:
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Avg Income", f"₹{safe_int(filtered_df['Income'].mean())}")
    col2.metric("Avg Total Spend", f"₹{safe_int(filtered_df['Total_Spend'].mean())}")
    col3.metric("Avg Web Visits / Month", safe_int(filtered_df['NumWebVisitsMonth'].mean()))
    col4.metric("Campaign Response Rate", safe_percent(filtered_df['Response'].mean()))

# --------------------------------------------------
# Visualization Section
# --------------------------------------------------
st.divider()
st.subheader("📈 Data Visualization")

if filtered_df.empty:
    st.info("No data available for visualization.")
else:
    fig, ax = plt.subplots(figsize=(7, 5))

    # BAR CHART
    if chart_type == "Bar Chart":
        sns.barplot(
            x=["Income", "Total Spend"],
            y=[
                filtered_df["Income"].mean(),
                filtered_df["Total_Spend"].mean()
            ],
            ax=ax
        )
        ax.set_title("Average Income vs Total Spend")

    # PIE CHART
    elif chart_type == "Pie Chart":
        values = [
            filtered_df["MntWines"].sum(),
            filtered_df["MntMeatProducts"].sum(),
            filtered_df["MntGoldProds"].sum()
        ]
        labels = ["Wine", "Meat", "Gold"]
        ax.pie(values, labels=labels, autopct="%1.1f%%")
        ax.set_title("Spending Distribution")

    # DONUT CHART
    elif chart_type == "Donut Chart":
        values = [
            filtered_df["NumWebPurchases"].sum(),
            filtered_df["NumStorePurchases"].sum(),
            filtered_df["NumCatalogPurchases"].sum()
        ]
        labels = ["Web", "Store", "Catalog"]
        ax.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            wedgeprops=dict(width=0.4)
        )
        ax.set_title("Purchase Channel Distribution")

    # BOX PLOT
    elif chart_type == "Box Plot":
        sns.boxplot(
            y=filtered_df["Total_Spend"],
            ax=ax
        )
        ax.set_title("Total Spend Distribution")

    # HISTOGRAM
    elif chart_type == "Histogram":
        sns.histplot(
            filtered_df["Income"],
            bins=20,
            kde=True,
            ax=ax
        )
        ax.set_title("Income Distribution")

    st.pyplot(fig)

# --------------------------------------------------
# Segment Summary Table
# --------------------------------------------------
st.divider()
st.subheader("📊 Segment Summary (Averages)")

if not filtered_df.empty:
    summary_df = filtered_df.agg({
        "Income": "mean",
        "Total_Spend": "mean",
        "Total_Purchases": "mean",
        "NumWebVisitsMonth": "mean",
        "Response": "mean"
    }).round(2)

    st.dataframe(summary_df.to_frame("Average Value"))
else:
    st.info("No summary available for this segment.")

# --------------------------------------------------
# Customer Data Preview
# --------------------------------------------------
st.divider()
st.subheader("🧾 Customer Records (Preview)")

if not filtered_df.empty:
    st.dataframe(filtered_df.head(50))
else:
    st.info("No customer records to display.")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption("Marketing Campaign Analysis | Interactive Visualization Dashboard")

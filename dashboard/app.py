import os
import pandas as pd
import streamlit as st
import plotly.express as px

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
def safe_mean(series):
    if series.dropna().empty:
        return "N/A"
    return round(series.mean(), 2)

def safe_percent(series):
    if series.dropna().empty:
        return "N/A"
    return f"{round(series.mean() * 100, 2)}%"

# --------------------------------------------------
# Load Data (CSV inside dashboard/)
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "final_marketing_data.csv")

try:
    df = pd.read_csv(DATA_PATH)
except Exception as e:
    st.error("❌ Unable to load final_marketing_data.csv")
    st.write("Expected path:", DATA_PATH)
    st.write("Error:", e)
    st.stop()

df = pd.read_csv(DATA_PATH)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("📊 Marketing Campaign Analysis Dashboard")
st.markdown(
    "Interactive dashboard with **rule-based segmentation** and **dynamic visualizations**."
)

# --------------------------------------------------
# Filters
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:
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

with col2:
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
# Segment Filtering
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
# KPIs
# --------------------------------------------------
st.subheader("📌 Key Performance Indicators")

if filtered_df.empty:
    st.warning("No data available for this segment.")
else:
    k1, k2, k3, k4 = st.columns(4)

    k1.metric("Avg Income", f"₹{safe_mean(filtered_df['Income'])}")
    k2.metric("Avg Total Spend", f"₹{safe_mean(filtered_df['Total_Spend'])}")
    k3.metric("Avg Web Visits", safe_mean(filtered_df["NumWebVisitsMonth"]))
    k4.metric("Response Rate", safe_percent(filtered_df["Response"]))

# --------------------------------------------------
# Visualization Section
# --------------------------------------------------
st.divider()
st.subheader("📈 Visualization")

if not filtered_df.empty:

    # BAR CHART
    if chart_type == "Bar Chart":
        chart_df = pd.DataFrame({
            "Metric": ["Income", "Total Spend"],
            "Value": [
                filtered_df["Income"].mean(),
                filtered_df["Total_Spend"].mean()
            ]
        })
        st.bar_chart(chart_df.set_index("Metric"))

    # PIE CHART (REAL)
    elif chart_type == "Pie Chart":
        pie_df = pd.DataFrame({
            "Category": ["Wine", "Meat", "Gold"],
            "Spend": [
                filtered_df["MntWines"].sum(),
                filtered_df["MntMeatProducts"].sum(),
                filtered_df["MntGoldProds"].sum()
            ]
        })

        fig = px.pie(
            pie_df,
            names="Category",
            values="Spend",
            title="Spending Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    # DONUT CHART (REAL)
    elif chart_type == "Donut Chart":
        donut_df = pd.DataFrame({
            "Channel": ["Web", "Store", "Catalog"],
            "Purchases": [
                filtered_df["NumWebPurchases"].sum(),
                filtered_df["NumStorePurchases"].sum(),
                filtered_df["NumCatalogPurchases"].sum()
            ]
        })

        fig = px.pie(
            donut_df,
            names="Channel",
            values="Purchases",
            hole=0.4,
            title="Purchase Channel Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    # BOX PLOT (SIMULATED DISTRIBUTION)
    elif chart_type == "Box Plot":
        st.bar_chart(filtered_df["Total_Spend"].value_counts().head(20))

    # HISTOGRAM
    elif chart_type == "Histogram":
        st.bar_chart(filtered_df["Income"].value_counts().head(20))


    # BOX PLOT (simulated via distribution)
    elif chart_type == "Box Plot":
        st.write("Total Spend Distribution")
        st.bar_chart(filtered_df["Total_Spend"].value_counts().head(20))

    # HISTOGRAM
    elif chart_type == "Histogram":
        st.write("Income Distribution")
        st.bar_chart(filtered_df["Income"].value_counts().head(20))

# --------------------------------------------------
# Table
# --------------------------------------------------
st.divider()
st.subheader("🧾 Customer Data Preview")
st.dataframe(filtered_df.head(50))

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption("Marketing Campaign Analysis | Interactive Streamlit Dashboard")

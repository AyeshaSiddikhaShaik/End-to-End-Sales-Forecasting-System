# Task 7 — Deployment: Interactive Dashboard using Streamlit
## 7.1 Import Required Libraries
# ============================================================
# Sales Forecasting Dashboard
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

from prophet import Prophet
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# ------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    layout="wide",
    page_icon="📊"
)

st.title("📊 Superstore Sales Forecasting Dashboard")
st.markdown("Interactive Dashboard for Sales Analysis, Forecasting, Anomaly Detection and Product Segmentation")

# ============================================================
# 7.2 Load Dataset
# ============================================================

df = pd.read_csv("train.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)
st.success("Dataset Loaded Successfully!")

# Time Features
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

# ============================================================
# 7.3 Sidebar
# ============================================================

page = st.sidebar.radio(
    "Select Dashboard",
    (
        "Sales Overview",
        "Forecast Explorer",
        "Anomaly Report",
        "Product Demand Segments"
    )
)

# ============================================================
# Sales Overview Dashboard
# ============================================================

if page == "Sales Overview":

    st.header("📈 Sales Overview Dashboard")

    yearly_sales = df.groupby("Year")["Sales"].sum().reset_index()

    fig = px.bar(
        yearly_sales,
        x="Year",
        y="Sales",
        title="Total Sales by Year"
    )

    st.plotly_chart(fig, use_container_width=True)

   monthly_sales = (
    df.groupby(pd.Grouper(key="Order Date", freq="MS"))["Sales"]
    .sum()
    .reset_index()
)

    fig2 = px.line(
        monthly_sales,
        x="Order Date",
        y="Sales",
        title="Monthly Sales Trend"
    )

    st.plotly_chart(fig2, use_container_width=True)

    region = st.selectbox(
        "Select Region",
        ["All"] + list(df["Region"].unique())
    )

    category = st.selectbox(
        "Select Category",
        ["All"] + list(df["Category"].unique())
    )

    filtered = df.copy()

    if region != "All":
        filtered = filtered[filtered["Region"] == region]

    if category != "All":
        filtered = filtered[filtered["Category"] == category]

    st.subheader("Filtered Data")

    st.dataframe(filtered.head(20))

    # ============================================================
# Forecast Explorer
# ============================================================

elif page == "Forecast Explorer":

    st.header("📈 Sales Forecast")

    monthly = (
        df.groupby(pd.Grouper(key="Order Date", freq="MS"))["Sales"]
        .sum()
        .reset_index()
    )

    prophet_df = monthly.rename(
        columns={
            "Order Date": "ds",
            "Sales": "y"
        }
    )

    model = Prophet()
    model.fit(prophet_df)

    future = model.make_future_dataframe(
        periods=6,
        freq="MS"
    )

    forecast = model.predict(future)

    fig1 = model.plot(forecast)

    st.pyplot(fig1, clear_figure=True)

    st.subheader("Next 6 Months Forecast")

    st.dataframe(
        forecast[["ds", "yhat"]].tail(6)
    )

    # ============================================================
# Anomaly Report
# ============================================================

elif page == "Anomaly Report":

    st.header("🚨 Sales Anomaly Detection")

    weekly = (
        df.groupby(pd.Grouper(key="Order Date", freq="W"))["Sales"]
        .sum()
        .reset_index()
    )

    iso = IsolationForest(
        contamination=0.05,
        random_state=42
    )

    weekly["Anomaly"] = iso.fit_predict(
        weekly[["Sales"]]
    )

    weekly["Status"] = weekly["Anomaly"].map(
        {
            1: "Normal",
            -1: "Anomaly"
        }
    )

    fig = px.scatter(
        weekly,
        x="Order Date",
        y="Sales",
        color="Status",
        title="Detected Sales Anomalies"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Detected Anomalies")

    st.dataframe(
        weekly[
            weekly["Status"]=="Anomaly"
        ]
    )

    # ============================================================
# Product Demand Segments
# ============================================================

elif page == "Product Demand Segments":

    st.header("🛒 Product Demand Segmentation")

    segment = (
        df.groupby("Sub-Category")
        .agg(
            Total_Sales=("Sales","sum"),
            Avg_Order_Value=("Sales","mean")
        )
        .reset_index()
    )

    kmeans = KMeans(
        n_clusters=4,
        random_state=42
    )

    segment["Cluster"] = kmeans.fit_predict(
        segment[
            [
                "Total_Sales",
                "Avg_Order_Value"
            ]
        ]
    )

    pca = PCA(n_components=2)

    comp = pca.fit_transform(
        segment[
            [
                "Total_Sales",
                "Avg_Order_Value"
            ]
        ]
    )

    segment["PC1"] = comp[:,0]
    segment["PC2"] = comp[:,1]

    fig = px.scatter(
        segment,
        x="PC1",
        y="PC2",
        color=segment["Cluster"].astype(str),
        text="Sub-Category",
        title="Product Demand Clusters"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Clustered Products")

    st.dataframe(segment)

    

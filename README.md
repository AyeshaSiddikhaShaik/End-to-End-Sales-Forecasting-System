# 📊 End-to-End Sales Forecasting & Demand Intelligence System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Forecasting-green)
![Prophet](https://img.shields.io/badge/Prophet-Time%20Series-blueviolet)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)
![Status](https://img.shields.io/badge/Project-Completed-success)

</div>

---

## 📌 Project Overview

This project presents a comprehensive **Sales Forecasting & Demand Intelligence System** developed using historical Superstore retail sales data.

The objective is to transform raw transactional data into actionable business intelligence through advanced analytics, forecasting models, anomaly detection, product demand segmentation, and an interactive Streamlit dashboard.

The project demonstrates an end-to-end Data Science workflow ranging from data preprocessing to deployment while addressing real-world retail business challenges.

---

# 🎯 Business Objectives

- 📈 Analyze historical sales performance
- 🔍 Discover hidden business insights through Exploratory Data Analysis (EDA)
- 📅 Forecast future sales using multiple forecasting models
- 🚨 Detect abnormal sales patterns using anomaly detection techniques
- 📦 Segment products based on demand characteristics
- 📊 Build an interactive Streamlit dashboard
- 💼 Generate actionable business recommendations for inventory optimization

---

# 🛠️ Technologies Used

| Category | Technologies |
|-----------|--------------|
| Programming | Python 3.x |
| Data Processing | Pandas, NumPy |
| Data Visualization | Matplotlib, Plotly |
| Statistical Forecasting | SARIMA (Statsmodels) |
| Machine Learning | XGBoost |
| Time Series Forecasting | Facebook Prophet |
| Clustering | K-Means |
| Anomaly Detection | Isolation Forest, Z-Score |
| Dashboard | Streamlit |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
SalesForecasting_Ayesha/
│
├── analysis.ipynb
├── app.py
├── train.csv
├── requirements.txt
├── summary.docx
├── charts/
└── README.md
```

---

# 📊 Project Workflow

### ✅ Task 1 — Data Loading & Exploration

- Data Cleaning
- Missing Value Analysis
- Duplicate Removal
- Feature Engineering
- Time-based Feature Extraction
- Business Insight Generation

---

### ✅ Task 2 — Time Series Analysis

- Monthly Sales Trend
- Time Series Decomposition
- Trend Analysis
- Seasonality Analysis
- Residual Analysis
- ADF Stationarity Test

---

### ✅ Task 3 — Sales Forecasting

Three forecasting approaches were developed and compared.

### 📈 SARIMA

- Statistical Time Series Model
- Seasonal Forecasting

### 🤖 Prophet

- Facebook Prophet
- Automatic Trend Detection
- Seasonality Modelling

### ⚡ XGBoost

- Lag Feature Engineering
- Machine Learning Forecasting
- Rolling Mean Features

Performance comparison was conducted using:

- MAE
- RMSE
- MAPE

---

### ✅ Task 4 — Category & Region Forecasting

Forecasts were generated separately for:

- Furniture
- Technology
- Office Supplies
- West Region
- East Region

---

### ✅ Task 5 — Anomaly Detection

Implemented:

- Isolation Forest
- Z-Score Detection

Detected unusual weekly sales spikes and abnormal demand periods.

---

### ✅ Task 6 — Product Demand Segmentation

Applied:

- K-Means Clustering
- PCA Visualization

Demand segments were created based on:

- Total Sales
- Sales Growth
- Sales Volatility
- Average Order Value

---

### ✅ Task 7 — Interactive Streamlit Dashboard

The dashboard contains four interactive pages:

📊 Sales Overview

🔮 Forecast Explorer

🚨 Anomaly Report

📦 Product Demand Segments

---

### ✅ Task 8 — Executive Business Report

Prepared a professional business report summarizing:

- Executive Summary
- Forecasting Results
- Business Insights
- Demand Segmentation
- Business Recommendations
- Project Limitations

---

# 📈 Forecasting Model Comparison

| Model | MAE | RMSE | MAPE (%) |
|------|------:|------:|------:|
| SARIMA | 13930.02 | 16394.82 | 27.77 |
| Prophet | **7717.23** | **9182.90** | **13.76** |
| XGBoost | 9490.47 | 12646.75 | 15.49 |

🏆 **Best Performing Model:** **Facebook Prophet**

---

# 💡 Key Business Insights

- Technology generated the highest overall revenue.
- Sales exhibited strong seasonal demand during year-end.
- Prophet delivered the most accurate sales forecasts.
- Weekly anomalies highlighted promotional and festive sales periods.
- Demand segmentation enables optimized inventory management.
- Interactive dashboards improve business decision-making.

---

# 🚀 Future Enhancements

- Deep Learning (LSTM) Forecasting
- Real-Time Sales Prediction
- Cloud Deployment
- Automated Data Pipeline
- Power BI Integration
- AI-based Inventory Optimization

---

# 👩‍💻 Author

**Shaik Ayesha Siddikha**

B.Tech – Artificial Intelligence & Data Science

---

## ⭐ If you found this project useful, consider giving it a star!

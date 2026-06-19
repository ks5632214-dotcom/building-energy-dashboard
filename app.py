import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Building Energy Dashboard",
    layout="wide"
)

st.title("🏢 Building Energy Consumption Analysis & Prediction")

st.markdown("""
This dashboard analyzes building energy consumption and compares ML models for forecasting.
""")

# -----------------------------
# LOAD DATA
# -----------------------------
results = pd.read_csv("model_comparison (1).csv")

best_model = results.sort_values(by="R2", ascending=False).iloc[0]

# -----------------------------
# KPI SECTION (UPGRADED)
# -----------------------------
st.header("📌 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("🏆 Best Model", best_model["Model"])
col2.metric("📈 R² Score", f"{best_model['R2']:.3f}")
col3.metric("📉 RMSE", f"{best_model['RMSE']:.2f}")

st.markdown("---")

# -----------------------------
# MODEL COMPARISON
# -----------------------------
st.header("📊 Model Comparison")
st.dataframe(results, use_container_width=True)

# -----------------------------
# LIVE PREDICTION SYSTEM (NEW ⭐)
# -----------------------------
st.header("⚡ Live Energy Consumption Prediction")

st.markdown("Enter values to estimate building energy consumption:")

col1, col2, col3 = st.columns(3)

temperature = col1.number_input("Temperature (°C)", value=25.0)
hour = col2.number_input("Hour of Day", min_value=0, max_value=23, value=12)
is_weekend = col3.selectbox("Is Weekend?", [0, 1])

# Simple rule-based demo (since trained model is not loaded in Streamlit)
# You can replace this later with actual model.pkl

predicted_energy = (
    50 +
    (temperature * 2) -
    (hour * 0.5) +
    (is_weekend * 10)
)

st.success(f"🔮 Estimated Energy Consumption: {predicted_energy:.2f} units")

st.markdown("---")

# -----------------------------
# EXPLORATORY ANALYSIS
# -----------------------------
st.header("📈 Energy Consumption Analysis")

st.subheader("Monthly Consumption")
st.image("Monthly_Median_Energy_Consumption.png")

st.subheader("Hourly Consumption")
st.image("Median Energy Consumption by Hour.png")

st.subheader("Weekly Pattern")
st.image("Median Energy Consumption by Day of Week.png")

st.subheader("Temperature Impact")
st.image("Temperature vs Energy Consumption.png")

# -----------------------------
# MODELs Matrix COMPARISON
# -----------------------------
st.header("🤖 Model Matrix Comparison")

tabs = st.tabs(["R² Comparison", "MAE Comparison", "RMSE Comparison"])

with tabs[0]:
    st.image("Model Comparison Based on R2.png")

with tabs[1]:
    st.image("Model Comparison Based on MAE.png")

with tabs[2]:
    st.image("Model Comparison Based on RMSE.png")

# -----------------------------
# MODEL PREDICTIONS
# -----------------------------
st.header("🤖 Model Predictions")

tabs = st.tabs(["Linear Model", "Random Forest", "XGBoost"])

with tabs[0]:
    st.image("LR Comparison.png")

with tabs[1]:
    st.image("RF Comparison.png")

with tabs[2]:
    st.image("XGB Comparison.png")


# -----------------------------
# BETTER CONCLUSION (IMPROVED ⭐)
# -----------------------------
st.header("📝 Conclusion")

st.write(f"""
The **{best_model['Model']}** performed best with an R² score of **{best_model['R2']:.3f}**.

### Why Random Forest Performed Best

- Captures complex non-linear relationships in energy consumption data.
- Handles interactions between building characteristics, time-based features, and historical consumption effectively.
- Robust to outliers and noisy observations commonly found in large-scale energy datasets.
- Reduces overfitting by combining predictions from multiple decision trees.
- Performs well on datasets with mixed feature types and complex patterns.

### Key Insights

- Historical energy consumption (Lag_1 and Lag_24) is the strongest predictor of future energy usage.
- Building characteristics such as surface area significantly influence consumption levels.
- Time-based features such as hour of day, day of week, and seasonal patterns contribute to prediction performance.
- Weather-related variables showed lower importance in the final model due to limited variation after data integration and preprocessing.
- Random Forest achieved the highest predictive accuracy with an R² score of 0.927, making it the most reliable model for forecasting building energy consumption in this study.
""")
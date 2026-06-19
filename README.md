# 🏢 Building Energy Consumption Forecasting

## 📌 Project Overview

This project focuses on forecasting building energy consumption using machine learning techniques. The objective is to analyze historical energy usage patterns, weather conditions, building characteristics, and calendar-based features to predict future energy consumption accurately.

The project includes:

* Data Integration and Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Machine Learning Model Development
* Model Comparison and Evaluation
* Streamlit Dashboard Deployment

---

## 🎯 Problem Statement

Building energy consumption is influenced by multiple factors such as:

* Historical energy usage
* Temperature and weather conditions
* Building characteristics
* Time and seasonal effects
* Holidays and weekends

Accurate forecasting helps improve:

* Energy efficiency
* Resource planning
* Cost optimization
* Smart building management

---

## 📂 Dataset Sources

The project combines multiple datasets:

### 1. Energy Consumption Data

Contains historical building energy consumption records.

### 2. Weather Data

Includes:

* Temperature
* Base Temperature

### 3. Building Metadata

Includes:

* Surface Area
* Distance
* Site Information

### 4. Holiday Data

Used to identify holiday effects on energy consumption.

---

## ⚙️ Data Preprocessing

The following preprocessing steps were performed:

### Data Integration

Merged:

* Energy data
* Weather data
* Metadata
* Holiday information

### Missing Value Handling

* Temperature values imputed using median values.
* Missing records removed where necessary.

### Feature Engineering

Created:

* Hour
* DayOfWeek
* Month
* WeekOfYear
* IsWeekend
* IsHoliday
* Lag_1 (Previous hour consumption)
* Lag_24 (Previous day same hour consumption)
* Temp_Deviation
* Temp_Squared

### Data Cleaning

* Removed duplicate records
* Removed invalid timestamps
* Handled missing values
* Generated lag features

---

## 📊 Exploratory Data Analysis

The following visualizations were created:

* Monthly Energy Consumption
* Hourly Energy Consumption
* Weekly Consumption Patterns
* Temperature vs Energy Consumption
* Feature Correlation Heatmap

### Key Observations

* Historical consumption strongly influences future consumption.
* Energy usage follows clear hourly and seasonal patterns.
* Building characteristics contribute significantly to prediction performance.
* Weather variables show weaker influence compared to historical consumption.

---

## 🤖 Machine Learning Models

Three regression models were implemented:

### 1. Linear Regression

Used as a baseline model.

Advantages:

* Simple and interpretable
* Fast training

Limitations:

* Struggles with complex non-linear relationships

---

### 2. Random Forest Regressor

Advantages:

* Captures non-linear relationships
* Robust against noise
* Handles feature interactions well

---

### 3. XGBoost Regressor

Advantages:

* Gradient boosting framework
* Excellent predictive performance
* Built-in regularization
* Handles complex patterns effectively

---

## 📈 Model Performance

| Model             | MAE   | RMSE  | R²    |
| ----------------- | ----- | ----- | ----- |
| Linear Regression | 1.440 | 1.955 | 0.106 |
| Random Forest     | 0.314 | 0.641 | 0.904 |
| XGBoost           | 0.310 | 0.616 | 0.911 |

### Best Model

🏆 **XGBoost**

Performance:

* MAE = 0.310
* RMSE = 0.616
* R² = 0.911

---

## 🔍 Feature Importance Insights

The most influential features were:

1. Lag_1
2. Surface
3. Lag_24
4. Hour
5. Month

### Key Insight

Historical consumption patterns (Lag_1 and Lag_24) are the strongest predictors of future energy consumption.

---

## 📊 Prediction Comparison

Predicted vs Actual plots were generated for:

* Linear Regression
* Random Forest
* XGBoost

These visualizations demonstrate that XGBoost tracks actual consumption patterns most accurately.

---

## 🌐 Streamlit Dashboard

An interactive dashboard was developed using Streamlit.

Features:

* KPI Display
* Model Comparison
* Energy Consumption Analysis
* Visualization Dashboard
* Prediction Results

---

## 🚀 Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* Streamlit

---

## 📁 Project Structure

```text
Building_Energy_Dashboard/
│
├── Building_Energy_Consumption_Forecasting.ipynb
├── Building_Energy_Consumption_Summary_Report.pdf
├── app.py
├── requirements.txt
├── model_comparison.csv
│
├── Images/
│   ├── EDA Charts
│   ├── Model Comparison Charts
│   ├── Prediction Plots
│
└── README.md
```

## 🔮 Future Enhancements

Given more time, the following improvements can be explored:

* Hyperparameter optimization using Optuna/GridSearchCV
* Additional weather features
* Deep Learning models (LSTM/GRU)
* Real-time prediction pipeline
* Cloud deployment
* Automated data ingestion
* Explainable AI using SHAP values

---

## 📝 Conclusion

This project successfully developed a machine learning pipeline for building energy consumption forecasting. Three regression models were evaluated, and XGBoost achieved the highest predictive accuracy with an R² score of 0.911.

The results demonstrate that historical consumption behavior and building characteristics are more influential than weather variables in predicting future energy usage. The final solution includes both a predictive model and an interactive Streamlit dashboard, making it suitable for practical energy management and monitoring applications.

# Demand Forecasting Benchmark Project

## Overview

This project presents a complete demand forecasting pipeline developed using Python, SQLite, and Machine Learning techniques. The objective is to evaluate and compare different forecasting approaches through a robust benchmark framework, identifying the best-performing model for inventory demand prediction.

The project simulates a real-world Supply Chain environment, including inventory transactions, product master data, and historical demand records.

---

## Project Objectives

* Develop an end-to-end demand forecasting solution.
* Compare statistical, machine learning, and time series forecasting models.
* Measure forecasting performance using industry-standard metrics.
* Generate future demand projections to support inventory planning and replenishment decisions.
* Build a portfolio-ready Data Science project focused on Supply Chain Analytics.

---

## Dataset

The database was generated using simulated inventory transactions over a multi-year period.

### Database Structure

#### Products

Contains product master data:

* Product ID
* Product Description
* Category
* Class
* Lead Time
* Unit Price

#### Inventory Movements

Contains historical inventory transactions:

* Transaction Date
* Transaction ID
* Product ID
* Movement Type (Inbound / Outbound)
* Quantity
* Total Value

#### Current Inventory

Contains current stock levels:

* Product ID
* Available Quantity
* Data update

---

## Technologies Used

### Programming Language

* Python 3.11+

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Statsmodels
* Prophet
* XGBoost
* SQLite3

---

## Forecasting Models Evaluated

### 1. Weighted Moving Average (WMA)

A benchmark model using weighted averages of recent periods.

**Advantages**

* Simple implementation
* Fast execution
* Easy interpretation

**Limitations**

* Cannot capture trends
* Cannot capture seasonality

---

### 2. Holt-Winters Exponential Smoothing

Captures level, trend, and seasonality.

**Advantages**

* Strong performance on seasonal series
* Computationally efficient

---

### 3. SARIMA

Seasonal AutoRegressive Integrated Moving Average.

**Advantages**

* Handles autocorrelation
* Captures seasonality
* Widely used in forecasting applications

---

### 4. Prophet

Developed by Meta for business forecasting applications.

**Advantages**

* Robust against missing values
* Automatic trend detection
* Easy seasonality handling

---

### 5. XGBoost

Machine Learning model using lag features and rolling statistics.

**Advantages**

* Captures non-linear relationships
* Often achieves high predictive performance

---

## Forecasting Workflow

### Step 1 – Data Extraction

Historical inventory movements are extracted from the SQLite database.

### Step 2 – Data Aggregation

Demand is aggregated at a monthly level based on outbound inventory transactions.

### Step 3 – Calendar Completion

Missing periods are filled to create a continuous time series.

### Step 4 – Feature Engineering

Additional features are generated:

* Lag variables
* Rolling averages
* Rolling standard deviations
* Trend indicators

### Step 5 – Train/Test Split

Historical data is separated into:

* Training Set
* Testing Set

### Step 6 – Walk-Forward Validation

Models are evaluated using rolling-origin forecasting.

This approach better simulates real-world forecasting conditions.

### Step 7 – Benchmark Evaluation

Each model is evaluated using the same validation framework.

### Step 8 – Best Model Selection

The model with the lowest forecasting error is selected.

### Step 9 – Future Forecast Generation

The selected model generates demand forecasts for future periods.

---

## Evaluation Metrics

### MAE

Mean Absolute Error

Measures the average magnitude of forecasting errors.

### RMSE

Root Mean Squared Error

Penalizes large forecasting errors.

### MAPE

Mean Absolute Percentage Error

Provides error interpretation in percentage terms.

Primary ranking metric used in this project.

---

## Project Structure

```text
Demand_Forecasting_Project/
│
├── data/
│   ├── raw/
│   
│
├── notebooks/
│   ├── Data_Exploration.ipynb
│   ├── Weighted_Moving_Average.ipynb
│   └── Model_Comparison.ipynb
|
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Example Outputs

### Historical Demand Analysis

* Monthly demand trends
* Seasonality patterns
* Demand variability

### Model Benchmark Dashboard

Comparison of:

* MAE
* RMSE
* MAPE

### Future Demand Forecast

Includes:

* Forecast values
* Confidence intervals
* Forecast visualization

---

## Business Impact

This solution can support:

* Inventory Optimization
* Demand Planning
* Procurement Planning
* Supply Chain Analytics
* Sales & Operations Planning (S&OP)

Potential benefits include:

* Reduced stockouts
* Lower inventory carrying costs
* Improved forecast accuracy
* Better purchasing decisions

---

## Future Improvements

Planned enhancements include:

* Hierarchical Forecasting
* Product Segmentation (ABC/XYZ)
* Deep Learning Models (LSTM)
* Automated Hyperparameter Tuning
* Forecast Monitoring Dashboard
* MLOps Deployment Pipeline

---

## Author

**Raniere Pereira**

Data Analyst | Supply Chain Analytics | Data Science

### Skills

* Python
* SQL
* Power BI
* Machine Learning
* Forecasting
* Supply Chain Analytics
* Inventory Management

### Contact

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

## License

This project is licensed under the MIT License.

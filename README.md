# CPI Time-Series Forecasting Using ARIMA(5,1,0)

## Overview

This repository presents a rigorous univariate time-series forecasting study of the Consumer Price Index (CPI) using an ARIMA(5,1,0) specification.

The objective is to:

- Implement statistically disciplined out-of-sample validation  
- Benchmark against a naive persistence model  
- Generate a forward 12-month CPI projection  
- Demonstrate leakage-safe forecasting methodology  

This project emphasizes methodological correctness rather than purely predictive performance.

---

## Dataset

- Frequency: Monthly  
- Total observations: 190 months (~15.8 years)  
- Target variable: CPI index level  

The dataset was chronologically indexed and strictly partitioned prior to model estimation.

---

## Methodology

### 1. Stationarity and Differencing

To remove long-run trend and induce stationarity, first differencing was applied:

$$
y'_t = y_t - y_{t-1}
$$

---

### 2. Model Specification

An ARIMA(5,1,0) model was selected:

- \( d = 1 \) → First differencing  
- \( p = 5 \) → Five autoregressive lags  
- \( q = 0 \) → No moving-average component  

The differenced model is defined as:

$$
y'_t = c + \phi_1 y'_{t-1} + \phi_2 y'_{t-2} + \phi_3 y'_{t-3} + \phi_4 y'_{t-4} + \phi_5 y'_{t-5} + \varepsilon_t
$$

where:

- \( c \) = constant  
- \( \phi_i \) = autoregressive coefficients  
- \( \varepsilon_t \) = white noise error term  

---

### 3. Validation Design (Leakage-Safe)

To simulate realistic forecasting conditions:

- **Training set:** First 178 months  
- **Test set:** Final 12 months (strictly held out)  

The model was fit exclusively on training data and used to forecast the unseen 12-month horizon.

No future information was used during estimation.

---

### 4. Benchmark Model

A naive persistence forecast was implemented as a baseline:

$$
\hat{y}_{t+1} = y_t
$$

This establishes a minimal predictive benchmark.

---

## Evaluation Metrics

Performance was assessed using standard out-of-sample error measures.

### Root Mean Squared Error (RMSE)

$$
RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
$$

### Mean Absolute Error (MAE)

$$
MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
$$

### Mean Absolute Percentage Error (MAPE)

$$
MAPE = \frac{100}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right|
$$

---

## Out-of-Sample Results

| Metric | ARIMA | Naive |
|--------|--------|--------|
| RMSE | 0.8921 | 5.3743 |
| MAE | 0.6927 | 4.7434 |
| MAPE | 0.21% | — |

The ARIMA model substantially outperforms the naive persistence benchmark, demonstrating strong short-term predictive accuracy under proper validation.

---

## Outputs

- `validation_plot.png` — 12-month holdout comparison (ARIMA vs Naive)  
- `future_forecast.png` — Forward 12-month CPI projection  
- `validation_metrics.md` — Numerical performance summary  

---

## Forecast Interpretation

The forward 12-month projection suggests continued CPI momentum consistent with recent inflation dynamics.

Forecast uncertainty increases with horizon length due to recursive error propagation.

---

## Limitations

- Linear structure assumption (may underperform during structural macroeconomic shocks)  
- No explicit seasonal modeling (SARIMA extension could be explored)  
- Optimized for short-term forecasting performance  

---
## Author

Meherab Hossain Shafin

Independent time-series forecasting study demonstrating statistically disciplined model validation and benchmark comparison for applied macroeconomic forecasting.

## Reproducibility

Install dependencies:

```bash
pip install pandas numpy matplotlib statsmodels scikit-learn
---

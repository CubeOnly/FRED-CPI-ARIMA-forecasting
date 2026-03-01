# CPI Forecasting Validation Metrics

## Model Information

- **Model:** ARIMA(5,1,0)  
- **Data Frequency:** Monthly  
- **Total Observations:** 190  
- **Training Period:** First 178 months  
- **Test Period:** Last 12 months (Out-of-Sample Holdout)

---

## Out-of-Sample Performance (12-Month Holdout)

| Metric        | ARIMA | Naive |
|---------------|--------|--------|
| **RMSE**      | 0.8921 | 5.3743 |
| **MAE**       | 0.6927 | 4.7434 |
| **MAPE**      | 0.21%  | — |

---

## Interpretation

The ARIMA(5,1,0) model significantly outperforms the naive persistence benchmark across all error metrics.  

The low RMSE and MAPE values indicate strong short-term forecasting accuracy and effective capture of CPI momentum dynamics.

**Evaluation was conducted using true out-of-sample validation to prevent data leakage and ensure realistic forecasting performance.**

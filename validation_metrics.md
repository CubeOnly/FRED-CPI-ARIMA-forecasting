CPI Forecasting Validation Metrics
===================================
Model: ARIMA(5,1,0)
Data Frequency: Monthly
Total Observations: 190
Training Period: First 178 months
Test Period: Last 12 months (Out-of-Sample)
--------------------------------------------------
Out-of-Sample Performance (12-Month Holdout)
ARIMA RMSE: 0.8921
Naive RMSE: 5.3743
ARIMA MAE:  0.6927
Naive MAE:  4.7434
MAPE: 0.21%
Interpretation:
The ARIMA(5,1,0) model significantly outperforms the naive persistence benchmark
across all error metrics. The low RMSE and MAPE values indicate strong short-term
forecasting accuracy and effective capture of CPI momentum dynamics.
**Evaluation was conducted using true out-of-sample validation to avoid data leakage.**

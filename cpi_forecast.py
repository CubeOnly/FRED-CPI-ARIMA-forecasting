import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 1. Data Loading & Cleaning
df = pd.read_csv('cpi_data.csv')
df['Value'] = pd.to_numeric(df['Value'].astype(str).str.replace(',', ''), errors='coerce')
df['Date'] = pd.to_datetime(df['Date'])
df = df.dropna(subset=['Value']).set_index('Date').sort_index()

# 2. STEP 1: Proper Train/Test Split

train = df['Value'][:-12]
test = df['Value'][-12:]

# 3. STEP 2: Fit Model ONLY on Training Data
print("🔄 Training model on historical data (In-Sample)...")
model = ARIMA(train, order=(5, 1, 0))
model_fit = model.fit()

# 4. STEP 3: Forecast 12 Months Ahead (Out-of-Sample)
forecast = model_fit.forecast(steps=12)
forecast = pd.Series(forecast.values, index=test.index)

# 5. STEP 4: Calculate TRUE Out-of-Sample Errors
mae = mean_absolute_error(test, forecast)
rmse = np.sqrt(mean_squared_error(test, forecast))
mape = np.mean(np.abs((test.values - forecast.values) / test.values)) * 100

# 6. STEP 5: Compare Against Naive Forecast
# Naive logic: "Next 12 months will stay exactly at the last known value"
naive_forecast_val = train.iloc[-1]
naive_predictions = np.repeat(naive_forecast_val, 12)

n_mae = mean_absolute_error(test, naive_predictions)
n_rmse = np.sqrt(mean_squared_error(test, naive_predictions))

# 7. Final Report
print("\n" + "="*40)
print("📊 FINAL VALIDATION REPORT (OUT-OF-SAMPLE)")
print("="*40)
print(f"ARIMA RMSE: {rmse:.4f}  |  Naive RMSE: {n_rmse:.4f}")
print(f"ARIMA MAE:  {mae:.4f}   |  Naive MAE:  {n_mae:.4f}")
print(f"TRUE MAPE:  {mape:.2f}%")
print("-"*40)

if rmse < n_rmse:
    print("✅ SUCCESS: ARIMA outperforms Naive Forecast.")
else:
    print("⚠️ WARNING: Naive Forecast is better; adjust (p,d,q).")
print("="*40)

# 8. Integrated Visualization
plt.figure(figsize=(12, 6))
plt.plot(train.index[-24:], train[-24:], label='Training Data (Last 2 yrs)', color='blue')
plt.plot(test.index, test, label='Actual Values (The Blind Test)', color='green', linewidth=2)
plt.plot(test.index, forecast, label='ARIMA Forecast', color='red', linestyle='--')
plt.plot(test.index, naive_predictions, label='Naive Forecast', color='gray', linestyle=':')
plt.title('Out-of-Sample Validation: ARIMA vs Naive Forecast')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 9. FINAL FUTURE FORECAST


print("\n🔮 Generating TRUE 12-Month Future Forecast...")

final_model = ARIMA(df['Value'], order=(5,1,0))
final_fit = final_model.fit()

future_forecast = final_fit.forecast(steps=12)

last_date = df.index[-1]
future_dates = pd.date_range(start=last_date + pd.DateOffset(months=1),
                             periods=12,
                             freq='M')

future_forecast = pd.Series(future_forecast.values, index=future_dates)

plt.figure(figsize=(12,6))
plt.plot(df.index[-36:], df['Value'][-36:], label="Historical (Last 3 yrs)")
plt.plot(future_forecast.index, future_forecast,
         label="Next 12-Month Forecast", linestyle='--', color='red')

plt.title("True CPI Forecast (Next 12 Months)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

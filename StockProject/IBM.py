import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import math
import matplotlib.pyplot as plt

# Load the CSV data
file_path = r"./input/prices-split-adjusted.csv"
data_df = pd.read_csv(file_path)

# Filter only IBM stock data
ibm_df = data_df[data_df['symbol'] == 'IBM']
ibm_df = ibm_df[['date', 'close']]  # Focus on 'date' and 'close' price

# Sort data by date
ibm_df['date'] = pd.to_datetime(ibm_df['date'])
ibm_df = ibm_df.sort_values('date')

# Normalize the data for LSTM
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(ibm_df['close'].values.reshape(-1, 1))


# Prepare the data for prediction
def create_dataset(data, look_back=15):
    X, Y = [], []
    for i in range(len(data) - look_back - 1):
        a = data[i:(i + look_back), 0]
        X.append(a)
        Y.append(data[i + look_back, 0])
    return np.array(X), np.array(Y)



look_back = 15
X, Y = create_dataset(scaled_data, look_back)
X = np.reshape(X, (X.shape[0], 1, X.shape[1]))

# Load the pre-trained model
model_path = r"C:\Pratham\programmingProjects\pythonProgrammes\Python-code-practice\StockProject\my_model.keras"
model = tf.keras.models.load_model(model_path)

# Predict the next 15 days
predictions = []
current_input = X[-1]  # Start with the last available data point

for x in range(15):
    prediction = model.predict(current_input, verbose=0)
    predictions.append(prediction[0, 0])

    # Update the input sequence with the predicted value
    current_input = np.append(current_input[0, 0, 1:], prediction[0, 0])
    current_input = current_input.reshape(1, 1, look_back)

# Invert the predictions to the original scale
predicted_values = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

# Plot the original data and predictions
plt.figure(figsize=(12, 6))
plt.plot(ibm_df['date'], ibm_df['close'], label="Actual IBM Stock Prices")
future_dates = pd.date_range(ibm_df['date'].iloc[-1], periods=15, freq='B')  # 15 future business days
plt.plot(future_dates, predicted_values, label="Predicted Prices", color='red')
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("IBM Stock Price Prediction")
plt.legend()
plt.show()

# Calculate Error (RMSE)
actual_last = ibm_df['close'].values[-15:]
if len(actual_last) == len(predicted_values):
    rmse = math.sqrt(mean_squared_error(actual_last, predicted_values[:, 0]))
    print(f"Model RMSE: {rmse:.2f}")
else:
    print("Not enough actual data for RMSE calculation.")

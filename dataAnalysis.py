import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('data.csv')
arr = df.to_numpy()


# ANALYSING DATA 

# Convert 'datetime' column to datetime type
df['datetime'] = pd.to_datetime(df['datetime'])

# Calculate short-term (e.g., 50 days) and long-term (e.g., 200 days) SMAs
short_window = 50
long_window = 200

df['SMA50'] = df['close'].rolling(window=short_window, min_periods=1).mean()
df['SMA200'] = df['close'].rolling(window=long_window, min_periods=1).mean()

# Create signals based on SMA crossovers
df['Signal'] = 0  # 0 represents no signal
df['Signal'][df['SMA50'] > df['SMA200']] = 1  # 1 represents buy signal
df['Signal'][df['SMA50'] < df['SMA200']] = -1  # -1 represents sell signal

# Plot the closing prices and SMAs
plt.figure(figsize=(10, 6))
plt.plot(df['datetime'], df['close'], label='Close Price')
plt.plot(df['datetime'], df['SMA50'], label=f'SMA{short_window}')
plt.plot(df['datetime'], df['SMA200'], label=f'SMA{long_window}')

# Plot buy signals
plt.plot(df[df['Signal'] == 1]['datetime'], df[df['Signal'] == 1]['SMA50'], '^', markersize=10, color='g', label='Buy Signal')

# Plot sell signals
plt.plot(df[df['Signal'] == -1]['datetime'], df[df['Signal'] == -1]['SMA50'], 'v', markersize=10, color='r', label='Sell Signal')

plt.title('Simple Moving Average Crossover Strategy')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()
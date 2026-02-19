
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

# Import Prophet for time series forecasting
try:
    from prophet import Prophet
except ImportError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "prophet"])
    from prophet import Prophet

# 1. Load the dataset (Google stock prices) from Excel
dataset_path = r"C:\Users\sachi\Downloads\archive\Google Dataset.xlsx"
df = pd.read_excel(dataset_path)

# 2. Prepare the data for Prophet
# Prophet expects columns: 'ds' (date) and 'y' (value to forecast)
df = df[["Month Starting", "Close"]]
df = df.rename(columns={"Month Starting": "ds", "Close": "y"})

# 3. Visualize the historical closing prices
plt.style.use("fivethirtyeight")
plt.figure(figsize=(16,8))
plt.title("Google Closing Stock Price")
plt.plot(df["ds"], df["y"])
plt.xlabel("Date", fontsize=18)
plt.ylabel("Close Price USD ($)", fontsize=18)
plt.show()

# 4. Create and fit the Prophet model
m = Prophet()
m.fit(df)

# 5. Make future predictions (next 365 days)
future = m.make_future_dataframe(periods=365)
predictions = m.predict(future)

# 6. Plot the forecast
m.plot(predictions)
plt.title("Prediction of GOOGLE Stock Price")
plt.xlabel("Date")
plt.ylabel("Closing Stock Price")
plt.show()

# 7. Plot forecast components (trend, yearly seasonality, etc.)
m.plot_components(predictions)
plt.show()
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import pandas_datareader as web  # Commented out due to compatibility error
import warnings

# Ensure prophet is installed and import it
try:
    from prophet import Prophet
except ImportError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "prophet"])
    from prophet import Prophet

# Load the dataset from the provided xlsx file
dataset_path = r"C:\Users\sachi\Downloads\archive\Google Dataset.xlsx"

df = pd.read_excel(dataset_path)
print("Columns in loaded DataFrame:", df.columns.tolist())


# Prepare data for Prophet: select and rename columns
df = df[["Month Starting", "Close"]]
df = df.rename(columns={"Month Starting": "ds", "Close": "y"})
print(df.head())

# Plot the Google Closing Stock Price
plt.style.use("fivethirtyeight")
plt.figure(figsize=(16,8))
plt.title("Google Closing Stock Price")
plt.plot(df["Close"])
plt.xlabel("Date", fontsize=18)
plt.ylabel("Close Price USD ($)", fontsize=18)
plt.show()

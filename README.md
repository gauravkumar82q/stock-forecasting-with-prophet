# Stock Price Prediction with Prophet

This project demonstrates how to use Facebook Prophet for time series forecasting of Google stock prices.

## Features
- Loads historical Google stock price data from an Excel file
- Visualizes historical closing prices
- Trains a Prophet model for forecasting
- Predicts and visualizes the next 365 days of stock prices
- Shows trend and seasonality components

## Requirements
- Python 3.8+
- pandas
- numpy
- matplotlib
- prophet
- openpyxl (for reading Excel files)

## How to Run
1. Clone or download this repository.
2. Place your dataset (Google Dataset.xlsx) in the `archive` folder or update the path in `stockprediction.py`.
3. (Recommended) Create and activate a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   Or let the script auto-install Prophet if missing.
5. Run the script:
   ```
   python stockprediction.py
   ```
   Or double-click `run_stock_prediction.bat`.

## File Structure
- `stockprediction.py` — Main script for data loading, modeling, and plotting
- `run_stock_prediction.bat` — Batch file to automate environment activation and script execution
- `archive/Google Dataset.xlsx` — Example dataset (not included; add your own)

## Output
- Plots of historical and predicted stock prices
- Prophet model component plots (trend, seasonality)

## Customization
- To use a different stock, replace the Excel file and update the path in the script.
- Change the `periods` parameter in `make_future_dataframe` for a different forecast horizon.

## License
This project is for educational purposes.

import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime

# Define API endpoints and parameters
gold_api = "https://api.goldapi.io/api/XAU/USD"
economic_api = "https://api.stlouisfed.org/fred/series/observations"
stock_api = "https://api.twelvedata.com/time_series"
currency_api = "https://api.exchangeratesapi.io/latest"

gold_api_key = "your-gold-api-key"
economic_api_key = "your-economic-api-key"
stock_api_key = "your-stock-api-key"
currency_api_key = "your-currency-api-key"

start_date = "2015-01-01"
end_date = datetime.today().strftime('%Y-%m-%d')

# Define function to get data from APIs
def get_data(api, api_key, params):
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    response = requests.get(api, headers=headers, params=params)
    return response.json()

# Get gold price data
gold_params = {
    "from": start_date,
    "to": end_date
}
gold_data = get_data(gold_api, gold_api_key, gold_params)

# Extract gold price and date data
gold_prices = [x["c"] for x in gold_data["data"]]
gold_dates = [x["d"] for x in gold_data["data"]]

# Create dataframe for gold prices and dates
gold_df = pd.DataFrame({"Time": gold_dates, "Gold_Price": gold_prices})

# Get economic indicator data
economic_params = {
    "series_id": "CPIAUCSL",
    "api_key": economic_api_key,
    "observation_start": start_date,
    "observation_end": end_date
}
economic_data = get_data(economic_api, "", economic_params)

# Extract economic indicator data
economic_df = pd.DataFrame(economic_data["observations"])
economic_df = economic_df[["date", "value"]]
economic_df = economic_df.rename(columns={"date": "Time", "value": "CPI"})

# Get stock market data
stock_params = {
    "symbol": "SPY",
    "interval": "1day",
    "apikey": stock_api_key,
    "start_date": start_date,
    "end_date": end_date
}
stock_data = get_data(stock_api, "", stock_params)

# Extract stock market data
stock_df = pd.DataFrame(stock_data["values"])
stock_df = stock_df[["datetime", "open", "close"]]
stock_df = stock_df.rename(columns={"datetime": "Time", "open": "SPY_Open", "close": "SPY_Close"})

# Get currency exchange rate data
currency_params = {
    "base": "USD",
    "symbols": "EUR,JPY,GBP,CAD,AUD",
    "access_key": currency_api_key
}
currency_data = get_data(currency_api, "", currency_params)

# Extract currency exchange rate data
currency_df = pd.DataFrame(currency_data["rates"], index=[0])
currency_df = currency_df.rename(columns={"EUR": "EUR_USD", "JPY": "JPY_USD", "GBP": "GBP_USD", "CAD": "CAD_USD", "AUD": "AUD_USD"})
currency_df["Time"] = datetime.today().strftime('%Y-%m-%d')

# Concatenate all dataframes
dfs = [gold_df, economic_df, stock_df, currency_df]
df = pd.concat(dfs)

import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

COMPANIES = {
    "INFY": "INFY.NS",
    "TCS": "TCS.NS",
    "RELIANCE": "RELIANCE.NS",
    "HDFCBANK": "HDFCBANK.NS",
}

START = (datetime.today() - timedelta(days=400)).strftime("%Y-%m-%d")
END = datetime.today().strftime("%Y-%m-%d")

all_data = []

for symbol, yf_symbol in COMPANIES.items():
    data = yf.download(yf_symbol, start=START, end=END)
    data = data.reset_index()
    data['Symbol'] = symbol
    data['Daily Return'] = (data['Close'] - data['Open']) / data['Open']
    data['7d MA'] = data['Close'].rolling(window=7).mean()
    # Custom metric: Volatility Score (stdev of returns in last 30 days)
    data['Volatility'] = data['Daily Return'].rolling(window=30).std()
    all_data.append(data)

df = pd.concat(all_data)
df['Date'] = pd.to_datetime(df['Date'])
# Drop rows with missing values
df = df.dropna()

df.to_csv('data/stocks.csv', index=False)
print("Data saved to data/stocks.csv")

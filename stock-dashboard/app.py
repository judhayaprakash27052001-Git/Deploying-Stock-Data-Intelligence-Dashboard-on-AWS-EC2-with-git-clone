from fastapi import FastAPI, Query
import pandas as pd
from typing import List
import uvicorn

app = FastAPI(title="Stock Data Intelligence Dashboard", description="Internship Assignment API", version="1.0")

df = pd.read_csv('data/stocks.csv', parse_dates=['Date'])

@app.get("/companies")
def get_companies():
    companies = df['Symbol'].unique().tolist()
    return {"companies": companies}

@app.get("/data/{symbol}")
def get_data(symbol: str):
    rows = df[df['Symbol'] == symbol].sort_values('Date')[-30:]
    return rows.to_dict(orient='records')

@app.get("/summary/{symbol}")
def get_summary(symbol: str):
    data = df[df['Symbol'] == symbol]
    high = data['Close'].max()
    low = data['Close'].min()
    avg = data['Close'].mean()
    return {"symbol": symbol, "52week_high": high, "52week_low": low, "avg_close": avg}

@app.get("/compare")
def compare_stocks(symbol1: str = Query(...), symbol2: str = Query(...)):
    data1 = df[df['Symbol'] == symbol1][-30:]
    data2 = df[df['Symbol'] == symbol2][-30:]
    # Simplified: Compare avg returns
    avg_return1 = data1['Daily Return'].mean()
    avg_return2 = data2['Daily Return'].mean()
    return {
        "symbol1": symbol1, "avg_return1": avg_return1,
        "symbol2": symbol2, "avg_return2": avg_return2
    }

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)

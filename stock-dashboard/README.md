# Stock Data Intelligence Dashboard

A mini financial data platform for internship assessment.

## Features

- Collects and cleans real or mock stock market data
- REST API endpoints for companies, data, summaries, and comparison
- (Bonus) Visualization dashboard with interactive charts

## Tech Stack

- Python
- FastAPI
- Pandas, NumPy
- SQLite
- Plotly/Chart.js (for dashboard)

## How to Run

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Run data collection & cleaning:
    ```
    python scripts/collect_data.py
    ```
3. Start backend server:
    ```
    uvicorn app:app --reload
    ```
4. (Optional) Open `static/index.html` for dashboard

## API Endpoints

| Endpoint                | Method | Description                                 |
|-------------------------|--------|---------------------------------------------|
| /companies              | GET    | Lists all available companies               |
| /data/{symbol}          | GET    | Last 30 days of data for a company          |
| /summary/{symbol}       | GET    | 52-week high, low, and avg close            |
| /compare                | GET    | Compare two stocks (`symbol1`, `symbol2`)   |

## Data Metrics

- Daily Return
- 7-day Moving Average
- 52-week High/Low
- Volatility Score (custom metric)

## Deployment

- Optionally deploy with Render/Oracle
- Docker setup included

---

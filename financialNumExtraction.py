import yfinance as yf
import pandas as pd

# | Method / Property           | What it gives you                                  |
# | --------------------------- | -------------------------------------------------- |
# | `ticker.info`               | Dictionary of current metadata (sector, P/E, etc.) |
# | `ticker.history()`          | Price/volume data over time                        |
# | `ticker.actions`            | Dividends and stock splits                         |
# | `ticker.dividends`          | Historical dividend payments                       |
# | `ticker.splits`             | Historical stock split data                        |
# | `ticker.earnings`           | Past earnings reports (yearly)                     |
# | `ticker.quarterly_earnings` | Quarterly earnings reports                         |
# | `ticker.financials`         | Income statement (yearly)                          |
# | `ticker.balance_sheet`      | Balance sheet (yearly)                             |
# | `ticker.cashflow`           | Cash flow statement (yearly)                       |
# | `ticker.calendar`           | Upcoming earnings date, ex-dividend date, etc.     |
# | `ticker.recommendations`    | Analyst recommendations                            |


# -----------------------------
# Config: Full Display in Console
# -----------------------------
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# -----------------------------
# Step 1: Load Ticker
# -----------------------------
ticker = yf.Ticker("AAPL")

# -----------------------------
# Step 2: Get Historical Data (5 Years)
# -----------------------------
hist = ticker.history(period="5y")

# Show in console
print(hist)

# Optional: Save to CSV
hist.to_csv("AAPL_5y_history.csv")

# -----------------------------
# Step 3: Optional - Explore Methods
# -----------------------------
# print(dir(ticker))  # Uncomment if you want to see all available attributes

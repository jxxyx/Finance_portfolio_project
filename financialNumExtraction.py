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
#later create a for loop/ array to run through multiple tickers

ticker = yf.Ticker("AAPL")

#past 5 years of price data
hist = ticker.history(period="5y")
df_hist = pd.DataFrame(hist)
#All the Net Income, Revenue, etc. are in the same dataframe
earning =  ticker.financials
df_earning = pd.DataFrame(earning)
#analyst recommendations, strongBuy, buy, hold, sell, strong sell
analyst_recs = ticker.recommendations
df_analyst_recs = pd.DataFrame(analyst_recs)


info = ticker.info
#example of how to access the single values
print(info['trailingPE'])


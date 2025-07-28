
# NOT IN USE RN. USING YFINANCE THROUGH PIP INSTALL

from dotenv import load_dotenv
import os
import http.client

load_dotenv()  # Load .env file

api_key = os.getenv("RAPIDAPI_KEY")


conn = http.client.HTTPSConnection("yahoo-finance15.p.rapidapi.com")

headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com"
}

conn.request(
    "GET", "/api/v1/markets/quote?ticker=AAPL&type=STOCKS", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

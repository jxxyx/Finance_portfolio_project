from yahoo_fin import news
from dotenv import load_dotenv
import os
import pandas as pd
import sys

# Ensure UTF-8 printing (especially for Windows terminals)
sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables (still good to keep for future use)
load_dotenv()

# ---------------------------------------
# 1. GET COMPANY-SPECIFIC NEWS (Yahoo RSS)
# ---------------------------------------
ticker = "AAPL"
rss_news = news.get_yf_rss(ticker)
rss_df = pd.DataFrame(rss_news)

print(f"✅ Pulled {len(rss_df)} articles for {ticker} via Yahoo RSS\n")
print(rss_df)

# Filter for Apple-specific headlines
filtered_df = rss_df[rss_df['title'].str.contains("Apple|AAPL", case=False, na=False)]

print(f"✅ {len(filtered_df)} Apple-related articles found")
print(filtered_df[["title", "link"]])


with pd.ExcelWriter("C:\\Users\\Howai\\OneDrive - Singapore Institute Of Technology\\side-projects\\Finance_portfolio_project\\apple_news_combined.xlsx") as writer:
    rss_df.to_excel(writer, sheet_name="Sector_News", index=False)
    filtered_df.to_excel(writer, sheet_name="Company_News", index=False)

print("✅ Saved sector and company news to 'apple_news_combined.xlsx'")


# # GETTING COMPANY RSI
# url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/indicators/rsi"

# querystring = {"symbol": "AAPL", "interval": "5m",
#                "series_type": "close", "time_period": "50", "limit": "50"}

# headers = {
#     "x-rapidapi-key": api_key,
#     "x-rapidapi-host": "yahoo-finance15.p.rapidapi.com"
# }

# rsi_response = requests.get(url, headers=headers, params=querystring)

# print(rsi_response.json())




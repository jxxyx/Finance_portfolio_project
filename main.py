import yfinance as yf
import pandas as pd
from feature_engineering import preprocess_data
from model import train_model

def main():
    # Example ticker
    ticker = yf.Ticker("AAPL")
    
    # Load historical price data
    df_hist = ticker.history(period="5y")
    df_hist.reset_index(inplace=True)
    
    # Feature Engineering
    df_processed = preprocess_data(df_hist)
    
    # Example: using Close price as feature and Open as target (adjust this)
    X = df_processed[['Close', 'High', 'Low', 'Volume']]
    y = (df_processed['Close'].shift(-1) > df_processed['Close']).astype(int)  # Up/Down label
    
    # Drop last row due to shift
    X = X[:-1]
    y = y[:-1]
    
    # Train model
    train_model(X, y)

if __name__ == "__main__":
    main()

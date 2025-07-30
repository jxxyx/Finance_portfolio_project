import yfinance as yf
import pandas as pd
from feature_engineering import preprocess_data
from model import train_model
import requests_cache

TICKERS = ['AAPL', 'MSFT', 'GOOGL']  # Add more tickers here if you want

def label_action(pct_change):
    if pct_change > 0.01:
        return 2  # Buy
    elif pct_change < -0.01:
        return 0  # Sell
    else:
        return 1  # Hold

def generate_rationale(signal):
    rationales = {
        0: "Sell - recent data indicates a potential downturn.",
        1: "Hold - minor movement detected, neutral outlook.",
        2: "Buy - upward momentum in recent price action."
    }
    return rationales.get(signal, "Unknown action")

def load_and_label_ticker(ticker, session):
    df_hist = yf.Ticker(ticker, session=session).history(period="3mo")
    if df_hist.empty:
        return None  # Skip if no data
    df_hist.reset_index(inplace=True)
    df_processed = preprocess_data(df_hist)
    df_processed['Date'] = pd.to_datetime(df_processed['Date'])
    df_processed['Ticker'] = ticker
    df_processed['pct_change'] = df_processed['Close'].pct_change().shift(-1)
    df_processed.dropna(inplace=True)
    df_processed['signal'] = df_processed['pct_change'].apply(label_action)
    return df_processed

def main():
    session = requests_cache.CachedSession('yfinance.cache', expire_after=1800)
    all_data = []

    for ticker in TICKERS:
        df = load_and_label_ticker(ticker, session)
        if df is not None:
            all_data.append(df)

    # Combine data from all tickers
    if not all_data:
        print("No data collected.")
        return

    df_combined = pd.concat(all_data).sort_values('Date').reset_index(drop=True)

    # Check if there's enough data
    if len(df_combined) < 50:
        print("Not enough data to train a model.")
        return

    # Time-based split
    split_idx = int(len(df_combined) * 0.7)
    train_data = df_combined.iloc[:split_idx]
    test_data = df_combined.iloc[split_idx:]

    print("Training size:", len(train_data), " | Testing size:", len(test_data))
    print("Class distribution in training set:")
    print(train_data['signal'].value_counts(normalize=True).rename({0: "Sell", 1: "Hold", 2: "Buy"}))

    # Features and Labels
    features = ['Close', 'High', 'Low', 'Volume']
    X_train = train_data[features]
    y_train = train_data['signal']
    X_test = test_data[features]
    y_test = test_data['signal']

    # Train model
    model, acc = train_model(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Output
    print("\n Buy / Hold / Sell Predictions:\n")
    for date, ticker, signal in zip(test_data['Date'], test_data['Ticker'], y_pred):
        action = ["Sell", "Hold", "Buy"][signal]
        rationale = generate_rationale(signal)
        print(f"{date.date()} — {ticker}: {action} — {rationale}")

if __name__ == "__main__":
    main()

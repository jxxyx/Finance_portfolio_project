# Finance_portfolio_project

#  Stock Price Movement Prediction (Buy / Hold / Sell Signals)

Welcome to my beginner-friendly machine learning project for predicting **stock price movements** and generating **Buy / Hold / Sell** investment signals based on historical data from Yahoo Finance.

This project showcases how machine learning can be applied to real-world stock data to assist in investment decisions — making it a valuable addition to any portfolio.

---

##  Project Overview

This Python-based project uses **historical stock price data** to train a machine learning model that predicts whether a stock's price will go **up or down** in the next period. Based on the prediction confidence, the model outputs investment actions:  
- **Buy** 📈 (price likely to go up)  
- **Hold** ⏸️ (uncertain / low confidence)  
- **Sell** 📉 (price likely to go down)

---

## 🔧 Tools & Libraries

- `Python 3.x`
- [`yfinance`](https://pypi.org/project/yfinance/) – for fetching historical stock data from Yahoo Finance
- `pandas`, `numpy` – data manipulation
- `scikit-learn` – machine learning models
- `matplotlib`, `seaborn` – (optional) data visualization

---

##  Features

- Fetches **historical stock prices** (daily or quarterly) using the `yfinance` API
- **Feature engineering**: Moving averages, momentum, volume trends
- Beginner-friendly ML models:
  - Logistic Regression
  - Decision Tree
  - Random Forest
- Generates **Buy / Hold / Sell signals** based on model prediction confidence
- Clean and readable code ideal for learning and portfolio showcase
- Extendable for future live data updates

---

##  How It Works

1. **Data Collection**  
   - Fetch historical data using `yfinance`
   - Choose from daily, weekly, or quarterly timeframes

2. **Preprocessing & Labeling**  
   - Create a binary label: `1` if next period's price goes up, `0` otherwise
   - Engineer features: past returns, moving averages, volume changes

3. **Model Training**  
   - Split data into training and test sets (time-based)
   - Train logistic regression, decision tree, and random forest models

4. **Prediction & Signal Generation**  
   - Use model to predict probabilities
   - Apply thresholds to convert probabilities into:
     - `Buy` if probability > 0.6
     - `Sell` if probability < 0.4
     - `Hold` otherwise

5. **Evaluation**  
   - Accuracy score
   - Optional: Confusion matrix, ROC curve

---

## ▶️ Getting Started

### 🔽 Installation

```bash
git clone 
cd 
pip install -r requirements.txt

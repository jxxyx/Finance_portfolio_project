import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    """
    Perform cleaning and feature engineering on the dataframe.
    """
    # Example of basic cleaning (adjust based on your notebook's logic)
    df = df.dropna()
    
    # Example scaling
    scaler = StandardScaler()
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    return df
import pandas as pd


def load_data(file_path):
    """
    Load dataset from CSV.
    """
    return pd.read_csv(file_path)


def remove_missing_values(df):
    """
    Remove rows with missing values.
    """
    return df.dropna()
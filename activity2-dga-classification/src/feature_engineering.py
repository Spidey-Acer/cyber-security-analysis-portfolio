"""Feature engineering helpers for DGA classification"""
import pandas as pd

def extract_length(df, column='domain'):
    df['length'] = df[column].str.len()
    return df

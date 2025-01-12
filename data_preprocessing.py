"""
Module: data_preprocessing.py
Author: Satej
Description:
This script handles data cleaning and preprocessing for the energy analytics project.
It ensures the energy usage data is clean, consistent, and ready for analysis.
"""

import pandas as pd
import numpy as np

def handle_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    """
    Handles missing values in the dataset.

    Args:
        data (pd.DataFrame): Input DataFrame with potential missing values.

    Returns:
        pd.DataFrame: Cleaned DataFrame with missing values handled.

    Strategy:
        - Numerical columns: Fill missing values with the median.
        - Categorical columns: Fill missing values with the mode.
    """
    for column in data.columns:
        if data[column].isnull().sum() > 0:
            if data[column].dtype in [np.float64, np.int64]:  # Numerical columns
                median_value = data[column].median()
                data[column].fillna(median_value, inplace=True)
                print(f"Filled missing values in numerical column '{column}' with median: {median_value}")
            else:  # Categorical columns
                mode_value = data[column].mode()[0]
                data[column].fillna(mode_value, inplace=True)
                print(f"Filled missing values in categorical column '{column}' with mode: {mode_value}")
    return data

def remove_anomalies(data: pd.DataFrame, column: str, threshold: float) -> pd.DataFrame:
    """
    Removes anomalies from a specified column based on a threshold.

    Args:
        data (pd.DataFrame): Input DataFrame with potential anomalies.
        column (str): Column name to check for anomalies.
        threshold (float): Threshold value to define anomalies (e.g., z-score).

    Returns:
        pd.DataFrame: Cleaned DataFrame with anomalies removed.
    """
    from scipy.stats import zscore

    data['z_score'] = zscore(data[column])  # Calculate z-scores for the column
    data_cleaned = data[data['z_score'].abs() <= threshold]  # Filter based on threshold
    print(f"Removed {len(data) - len(data_cleaned)} anomalies from column '{column}' based on z-score threshold of {threshold}.")
    data_cleaned.drop(columns=['z_score'], inplace=True)
    return data_cleaned

def preprocess_energy_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Performs full preprocessing pipeline on the energy data.

    Steps:
        - Handle missing values.
        - Remove anomalies.

    Args:
        data (pd.DataFrame): Raw input DataFrame.

    Returns:
        pd.DataFrame: Preprocessed DataFrame ready for analysis.
    """
    print("Starting data preprocessing...")
    data = handle_missing_values(data)
    # Remove anomalies from 'energy_usage' column with a z-score threshold of 3
    if 'energy_usage' in data.columns:
        data = remove_anomalies(data, column='energy_usage', threshold=3.0)
    print("Data preprocessing completed.")
    return data

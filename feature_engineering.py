"""
Module: feature_engineering.py
Author: Satej
Description:
This script handles feature engineering for the energy analytics project.
It creates new features to enhance predictive models, such as average daily consumption
and peak-hour usage, and categorizes households based on energy consumption tiers.
"""

import pandas as pd

def create_time_features(data: pd.DataFrame, timestamp_column: str) -> pd.DataFrame:
    """
    Creates time-based features such as hour, day, and month from a timestamp column.

    Args:
        data (pd.DataFrame): Input DataFrame with a timestamp column.
        timestamp_column (str): Column containing timestamp values.

    Returns:
        pd.DataFrame: DataFrame with new time-based features added.

    Example Usage:
        data = create_time_features(data, 'timestamp')
    """
    data['hour'] = pd.to_datetime(data[timestamp_column]).dt.hour
    data['day_of_week'] = pd.to_datetime(data[timestamp_column]).dt.dayofweek
    data['month'] = pd.to_datetime(data[timestamp_column]).dt.month
    print("Time-based features created: ['hour', 'day_of_week', 'month']")
    return data

def calculate_daily_consumption(data: pd.DataFrame, timestamp_column: str, usage_column: str) -> pd.DataFrame:
    """
    Calculates daily energy consumption for each household.

    Args:
        data (pd.DataFrame): Input DataFrame with timestamp and usage columns.
        timestamp_column (str): Column containing timestamp values.
        usage_column (str): Column containing energy usage values.

    Returns:
        pd.DataFrame: DataFrame with daily energy consumption added.

    Example Usage:
        data = calculate_daily_consumption(data, 'timestamp', 'energy_usage')
    """
    data['date'] = pd.to_datetime(data[timestamp_column]).dt.date
    daily_consumption = data.groupby('date')[usage_column].sum().reset_index()
    daily_consumption.rename(columns={usage_column: 'daily_consumption'}, inplace=True)
    print("Daily energy consumption calculated.")
    return daily_consumption

def categorize_consumption(data: pd.DataFrame, usage_column: str, bins: list, labels: list) -> pd.DataFrame:
    """
    Categorizes households into consumption tiers (e.g., low, medium, high).

    Args:
        data (pd.DataFrame): Input DataFrame with energy usage data.
        usage_column (str): Column containing energy usage values.
        bins (list): List of bin edges for categorization.
        labels (list): List of labels for each category.

    Returns:
        pd.DataFrame: DataFrame with a new column 'consumption_tier' added.

    Example Usage:
        data = categorize_consumption(data, 'energy_usage', [0, 50, 150, 500], ['Low', 'Medium', 'High'])
    """
    data['consumption_tier'] = pd.cut(data[usage_column], bins=bins, labels=labels, include_lowest=True)
    print("Consumption tiers categorized: ['Low', 'Medium', 'High']")
    return data

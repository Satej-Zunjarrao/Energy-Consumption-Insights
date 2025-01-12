"""
Module: eda.py
Author: Satej
Description:
This script performs exploratory data analysis (EDA) for the energy analytics project.
It includes visualizations and statistical summaries to uncover patterns, trends,
and relationships in the energy usage data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_energy_usage_trends(data: pd.DataFrame, date_column: str, usage_column: str):
    """
    Plots energy usage trends over time.

    Args:
        data (pd.DataFrame): DataFrame containing energy usage data.
        date_column (str): Column representing date/time values.
        usage_column (str): Column representing energy usage values.

    Example Usage:
        plot_energy_usage_trends(data, 'timestamp', 'energy_usage')
    """
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=date_column, y=usage_column, data=data)
    plt.title('Energy Usage Over Time')
    plt.xlabel('Date')
    plt.ylabel('Energy Usage (kWh)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_peak_hours(data: pd.DataFrame, time_column: str, usage_column: str):
    """
    Plots average energy usage by hour to identify peak consumption times.

    Args:
        data (pd.DataFrame): DataFrame containing energy usage data.
        time_column (str): Column representing time of day.
        usage_column (str): Column representing energy usage values.

    Example Usage:
        plot_peak_hours(data, 'hour', 'energy_usage')
    """
    data['hour'] = pd.to_datetime(data[time_column]).dt.hour
    hourly_usage = data.groupby('hour')[usage_column].mean()
    
    plt.figure(figsize=(10, 5))
    hourly_usage.plot(kind='bar', color='skyblue')
    plt.title('Average Energy Usage by Hour')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Average Energy Usage (kWh)')
    plt.grid(axis='y')
    plt.show()

def summarize_data(data: pd.DataFrame):
    """
    Prints a summary of the dataset, including missing values and descriptive statistics.

    Args:
        data (pd.DataFrame): Input DataFrame.
    """
    print("Dataset Summary:")
    print(data.info())
    print("\nDescriptive Statistics:")
    print(data.describe())
    print("\nMissing Values:")
    print(data.isnull().sum())

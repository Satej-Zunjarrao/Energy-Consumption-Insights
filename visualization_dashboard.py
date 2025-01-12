"""
Module: visualization_dashboard.py
Author: Satej
Description:
This script prepares and exports data for visualization in Tableau. It includes generating
key insights and saving processed data for integration with Tableau dashboards.
"""

import pandas as pd
import matplotlib.pyplot as plt

def export_dashboard_data(data: pd.DataFrame, export_path: str):
    """
    Exports processed data for Tableau visualization.

    Args:
        data (pd.DataFrame): DataFrame containing data to export.
        export_path (str): File path to save the exported data.

    Example Usage:
        export_dashboard_data(data, "C:/Users/Satej/Data/dashboard_data.csv")
    """
    try:
        data.to_csv(export_path, index=False)
        print(f"Dashboard data exported successfully to {export_path}.")
    except Exception as e:
        print("Error exporting dashboard data.")
        raise e

def generate_usage_summary(data: pd.DataFrame, group_by_column: str, usage_column: str) -> pd.DataFrame:
    """
    Generates a summary of energy usage grouped by a specific column.

    Args:
        data (pd.DataFrame): DataFrame containing energy usage data.
        group_by_column (str): Column to group data by (e.g., household, appliance).
        usage_column (str): Column representing energy usage.

    Returns:
        pd.DataFrame: DataFrame containing grouped summary data.

    Example Usage:
        summary = generate_usage_summary(data, 'appliance', 'energy_usage')
    """
    summary = data.groupby(group_by_column)[usage_column].sum().reset_index()
    summary.rename(columns={usage_column: 'total_usage'}, inplace=True)
    print(f"Generated usage summary grouped by '{group_by_column}'.")
    return summary

def plot_usage_summary(summary: pd.DataFrame, group_by_column: str, usage_column: str):
    """
    Visualizes the energy usage summary with a bar chart.

    Args:
        summary (pd.DataFrame): DataFrame containing summarized data.
        group_by_column (str): Column representing the grouping.
        usage_column (str): Column representing total usage values.

    Example Usage:
        plot_usage_summary(summary, 'appliance', 'total_usage')
    """
    plt.figure(figsize=(10, 6))
    plt.bar(summary[group_by_column], summary[usage_column], color='skyblue')
    plt.title(f"Energy Usage Summary by {group_by_column.capitalize()}")
    plt.xlabel(group_by_column.capitalize())
    plt.ylabel('Total Energy Usage (kWh)')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

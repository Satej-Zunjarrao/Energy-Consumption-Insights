"""
Module: data_collection.py
Author: Satej
Description:
This script handles the data collection process for the energy analytics project.
It gathers energy usage data from a specified data source (e.g., smart meter logs).
The script supports reading from local files, APIs, or databases.
"""

import pandas as pd

def load_energy_data(file_path: str) -> pd.DataFrame:
    """
    Loads energy usage data from a specified file path.

    Args:
        file_path (str): Path to the CSV file containing energy usage data.

    Returns:
        pd.DataFrame: DataFrame containing the energy usage data.

    Example Usage:
        df = load_energy_data("C:/Users/Satej/Data/energy_data.csv")
    """
    try:
        # Reading data from a CSV file
        data = pd.read_csv(file_path)
        print(f"Data successfully loaded from {file_path}")
        return data
    except FileNotFoundError as e:
        print(f"Error: File not found at {file_path}")
        raise e
    except Exception as e:
        print("An unexpected error occurred while loading data.")
        raise e

def fetch_data_from_api(api_url: str, headers: dict = None) -> pd.DataFrame:
    """
    Fetches energy usage data from an API.

    Args:
        api_url (str): API endpoint URL to fetch data from.
        headers (dict): Optional HTTP headers for authentication.

    Returns:
        pd.DataFrame: DataFrame containing the fetched data.

    Example Usage:
        df = fetch_data_from_api("https://api.example.com/energy_data", headers={"Authorization": "Bearer token"})
    """
    import requests

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = pd.DataFrame(response.json())
        print(f"Data successfully fetched from API: {api_url}")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {api_url}")
        raise e

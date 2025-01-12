"""
Module: main.py
Author: Satej
Description:
This script orchestrates the entire energy analytics project. It connects all modules,
manages the workflow, and ensures data flows seamlessly through each stage.
"""

from data_collection import load_energy_data
from data_preprocessing import preprocess_energy_data
from eda import summarize_data, plot_energy_usage_trends, plot_peak_hours
from feature_engineering import create_time_features, calculate_daily_consumption, categorize_consumption
from predictive_modeling import train_regression_model, train_classification_model
from visualization_dashboard import export_dashboard_data, generate_usage_summary, plot_usage_summary

def main():
    """
    Main function to execute the energy analytics project workflow.
    """
    # Step 1: Load raw energy data
    data_file_path = "C:/Users/Satej/Data/energy_data.csv"
    print("Loading energy usage data...")
    raw_data = load_energy_data(data_file_path)
    
    # Step 2: Preprocess the data
    print("Preprocessing energy usage data...")
    processed_data = preprocess_energy_data(raw_data)
    
    # Step 3: Perform Exploratory Data Analysis (EDA)
    print("Performing exploratory data analysis...")
    summarize_data(processed_data)
    plot_energy_usage_trends(processed_data, 'timestamp', 'energy_usage')
    plot_peak_hours(processed_data, 'timestamp', 'energy_usage')
    
    # Step 4: Feature Engineering
    print("Engineering features...")
    processed_data = create_time_features(processed_data, 'timestamp')
    daily_data = calculate_daily_consumption(processed_data, 'timestamp', 'energy_usage')
    categorized_data = categorize_consumption(processed_data, 'energy_usage', [0, 50, 150, 500], ['Low', 'Medium', 'High'])
    
    # Step 5: Train Predictive Models
    print("Training predictive models...")
    regression_model, mse = train_regression_model(processed_data, ['hour', 'temperature'], 'energy_usage')
    classification_model, report = train_classification_model(processed_data, ['hour', 'temperature'], 'high_usage_flag')
    
    # Step 6: Prepare Data for Visualization
    print("Preparing data for visualization...")
    usage_summary = generate_usage_summary(processed_data, 'appliance', 'energy_usage')
    export_dashboard_data(usage_summary, "C:/Users/Satej/Data/dashboard_data.csv")
    plot_usage_summary(usage_summary, 'appliance', 'total_usage')
    
    print("Energy analytics project workflow completed successfully.")

# Run the main function
if __name__ == "__main__":
    main()

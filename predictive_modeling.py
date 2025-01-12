"""
Module: predictive_modeling.py
Author: Satej
Description:
This script handles predictive modeling for the energy analytics project.
It includes regression models for forecasting energy usage and classification models
to identify high-consumption households.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, classification_report

def train_regression_model(data: pd.DataFrame, features: list, target: str):
    """
    Trains a regression model to forecast energy usage.

    Args:
        data (pd.DataFrame): Input DataFrame containing features and target variable.
        features (list): List of feature column names.
        target (str): Target column name for regression.

    Returns:
        tuple: Trained model and the mean squared error on the test set.

    Example Usage:
        model, mse = train_regression_model(data, ['hour', 'temperature'], 'energy_usage')
    """
    X = data[features]
    y = data[target]
    
    # Splitting data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Training a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predicting on the test set
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Regression Model MSE: {mse}")
    return model, mse

def train_classification_model(data: pd.DataFrame, features: list, target: str):
    """
    Trains a classification model to identify high-consumption households.

    Args:
        data (pd.DataFrame): Input DataFrame containing features and target variable.
        features (list): List of feature column names.
        target (str): Target column name for classification.

    Returns:
        tuple: Trained model and classification report on the test set.

    Example Usage:
        model, report = train_classification_model(data, ['hour', 'temperature'], 'high_usage_flag')
    """
    X = data[features]
    y = data[target]
    
    # Splitting data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Training a Random Forest classifier
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Predicting on the test set
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    print("Classification Report:\n", report)
    return model, report

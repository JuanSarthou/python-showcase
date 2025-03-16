#!/usr/bin/env python3

"""
CSV Data Exploration Template

This script provides a template for exploring CSV files using Pandas and Seaborn.
It performs basic data exploration tasks and creates common visualizations.

Usage:
    python3 explore_csv.py path/to/your_data.csv
"""

import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load CSV file into a Pandas DataFrame.
    
    Parameters:
        file_path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.\n")
        return df
    except Exception as e:
        print("Error loading CSV file:", e)
        exit(1)

def basic_exploration(df):
    """
    Perform basic exploration of the DataFrame.
    
    This function prints information about the data, including:
        - DataFrame info (data types, non-null counts)
        - First and last few rows
        - Descriptive statistics
        - Count of missing values
        - List of column names
    """
    print("----- Data Information -----")
    print(df.info())
    print("\n----- First 5 Rows -----")
    print(df.head())
    print("\n----- Last 5 Rows -----")
    print(df.tail())
    print("\n----- Descriptive Statistics -----")
    print(df.describe(include='all'))
    print("\n----- Missing Values -----")
    print(df.isnull().sum())
    print("\n----- Column Names -----")
    print(df.columns.tolist())
    print("\n")

def plot_distributions(df):
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[col].dropna(), kde=True, bins=30)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.tight_layout()
        # Save the plot instead of showing it
        plt.savefig(f'{col}_distribution.png')  # Save the plot as a .png file
        plt.close()  # Close the figure to prevent memory issues

def plot_pairwise_relationships(df):
    numeric_cols = df.select_dtypes(include=['number']).columns
    if len(numeric_cols) > 1:
        sns.pairplot(df[numeric_cols].dropna())
        plt.suptitle("Pairwise Relationships", y=1.02)
        # Save the plot instead of showing it
        plt.savefig('pairwise_relationships.png')
        plt.close()

def plot_correlation_heatmap(df):
    numeric_df = df.select_dtypes(include=['number'])
    if not numeric_df.empty:
        plt.figure(figsize=(10, 8))
        corr = numeric_df.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title("Correlation Heatmap")
        # Save the plot instead of showing it
        plt.savefig('correlation_heatmap.png')
        plt.close()

def main():
    # Parse command-line arguments for the CSV file path.
    parser = argparse.ArgumentParser(description='CSV Data Exploration Template')
    parser.add_argument('csv_file', type=str, help='Path to the CSV file')
    args = parser.parse_args()
    
    # Load the CSV file into a DataFrame.
    df = load_data(args.csv_file)
    
    # Perform basic data exploration.
    basic_exploration(df)
    
    # Create common visualizations.
    plot_distributions(df)
    plot_pairwise_relationships(df)
    plot_correlation_heatmap(df)

if __name__ == "__main__":
    main()

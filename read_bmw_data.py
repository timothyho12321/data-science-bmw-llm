"""
Script to read BMW sales data from Excel file
"""

import pandas as pd
import os

def read_bmw_sales_data(file_path):
    """
    Read BMW sales data from Excel file
    
    Parameters:
    -----------
    file_path : str
        Path to the Excel file
        
    Returns:
    --------
    pd.DataFrame
        DataFrame containing the BMW sales data
    """
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Display basic information about the dataset
        print(f"Successfully loaded data from: {file_path}")
        print(f"\nDataset shape: {df.shape[0]} rows, {df.shape[1]} columns")
        print(f"\nColumn names:")
        print(df.columns.tolist())
        print(f"\nFirst few rows:")
        print(df.head())
        print(f"\nData types:")
        print(df.dtypes)
        print(f"\nBasic statistics:")
        print(df.describe())
        
        return df
        
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        print("Please make sure the Excel file is in the correct location.")
        return None
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None


if __name__ == "__main__":
    # Define the path to the Excel file
    file_path = os.path.join("data-bmw", "BMW sales data (2020-2024).xlsx")
    
    # Read the data
    bmw_data = read_bmw_sales_data(file_path)
    
    if bmw_data is not None:
        print("\n" + "="*50)
        print("Data loaded successfully!")
        print("="*50)
        
        # Additional data exploration
        print(f"\nMissing values:")
        print(bmw_data.isnull().sum())
        
        # Display unique values for categorical columns
        categorical_columns = ['Model', 'Region', 'Color', 'Fuel_Type', 'Transmission']
        print(f"\nUnique values in categorical columns:")
        for col in categorical_columns:
            if col in bmw_data.columns:
                print(f"\n{col}: {bmw_data[col].nunique()} unique values")
                print(bmw_data[col].unique()[:10])  # Show first 10 unique values

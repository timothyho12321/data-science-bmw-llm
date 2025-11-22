"""
Script to read, clean, and preprocess BMW sales data for analysis
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime

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


def clean_and_preprocess_data(df):
    """
    Clean and preprocess BMW sales data for analysis
    
    Parameters:
    -----------
    df : pd.DataFrame
        Raw BMW sales data
        
    Returns:
    --------
    pd.DataFrame
        Cleaned and preprocessed DataFrame
    """
    print("\n" + "="*70)
    print("DATA CLEANING AND PREPROCESSING")
    print("="*70)
    
    # Create a copy to avoid modifying the original
    cleaned_df = df.copy()
    
    # 1. Remove completely blank rows
    initial_rows = len(cleaned_df)
    cleaned_df = cleaned_df.dropna(how='all')
    blank_rows_removed = initial_rows - len(cleaned_df)
    print(f"\n1. Removed {blank_rows_removed} completely blank rows")
    
    # 2. Remove duplicate rows
    duplicates_before = cleaned_df.duplicated().sum()
    cleaned_df = cleaned_df.drop_duplicates()
    print(f"2. Removed {duplicates_before} duplicate rows")
    
    # 3. Handle missing values in individual columns
    missing_before = cleaned_df.isnull().sum().sum()
    if missing_before > 0:
        print(f"\n3. Handling {missing_before} missing values:")
        for col in cleaned_df.columns:
            missing_count = cleaned_df[col].isnull().sum()
            if missing_count > 0:
                print(f"   - {col}: {missing_count} missing values")
                
                # Strategy: Drop rows with missing critical values
                if col in ['Model', 'Year', 'Region', 'Price_USD', 'Sales_Volume']:
                    cleaned_df = cleaned_df.dropna(subset=[col])
                    print(f"     → Dropped rows with missing {col}")
                # Fill missing categorical values with mode
                elif col in ['Color', 'Fuel_Type', 'Transmission']:
                    mode_value = cleaned_df[col].mode()[0]
                    cleaned_df[col].fillna(mode_value, inplace=True)
                    print(f"     → Filled with mode: {mode_value}")
                # Fill missing numerical values with median
                elif col in ['Engine_Size_L', 'Mileage_KM']:
                    median_value = cleaned_df[col].median()
                    cleaned_df[col].fillna(median_value, inplace=True)
                    print(f"     → Filled with median: {median_value}")
    else:
        print("\n3. No missing values found")
    
    # 4. Remove outliers using IQR method for numerical columns
    print("\n4. Detecting and handling outliers:")
    numerical_cols = ['Engine_Size_L', 'Mileage_KM', 'Price_USD', 'Sales_Volume']
    outliers_removed = 0
    
    for col in numerical_cols:
        Q1 = cleaned_df[col].quantile(0.25)
        Q3 = cleaned_df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 3 * IQR  # Using 3*IQR for less aggressive outlier removal
        upper_bound = Q3 + 3 * IQR
        
        outliers_count = ((cleaned_df[col] < lower_bound) | (cleaned_df[col] > upper_bound)).sum()
        cleaned_df = cleaned_df[(cleaned_df[col] >= lower_bound) & (cleaned_df[col] <= upper_bound)]
        outliers_removed += outliers_count
        
        if outliers_count > 0:
            print(f"   - {col}: Removed {outliers_count} outliers (range: {lower_bound:.2f} - {upper_bound:.2f})")
    
    print(f"   Total outliers removed: {outliers_removed}")
    
    # 5. Standardize text data (strip whitespace, consistent casing)
    print("\n5. Standardizing text data:")
    text_columns = ['Model', 'Region', 'Color', 'Fuel_Type', 'Transmission']
    for col in text_columns:
        if col in cleaned_df.columns:
            cleaned_df[col] = cleaned_df[col].str.strip()
            # Check for inconsistent casing
            unique_before = cleaned_df[col].nunique()
            cleaned_df[col] = cleaned_df[col].str.title()
            unique_after = cleaned_df[col].nunique()
            if unique_before != unique_after:
                print(f"   - {col}: Standardized casing ({unique_before} -> {unique_after} unique values)")
    
    # 6. Validate data ranges and business logic
    print("\n6. Validating data ranges:")
    validation_issues = 0
    
    # Year should be between 2020-2024
    invalid_years = cleaned_df[(cleaned_df['Year'] < 2020) | (cleaned_df['Year'] > 2024)]
    if len(invalid_years) > 0:
        cleaned_df = cleaned_df[(cleaned_df['Year'] >= 2020) & (cleaned_df['Year'] <= 2024)]
        validation_issues += len(invalid_years)
        print(f"   - Removed {len(invalid_years)} rows with invalid years")
    
    # Price should be positive
    invalid_prices = cleaned_df[cleaned_df['Price_USD'] <= 0]
    if len(invalid_prices) > 0:
        cleaned_df = cleaned_df[cleaned_df['Price_USD'] > 0]
        validation_issues += len(invalid_prices)
        print(f"   - Removed {len(invalid_prices)} rows with invalid prices")
    
    # Sales volume should be positive
    invalid_sales = cleaned_df[cleaned_df['Sales_Volume'] <= 0]
    if len(invalid_sales) > 0:
        cleaned_df = cleaned_df[cleaned_df['Sales_Volume'] > 0]
        validation_issues += len(invalid_sales)
        print(f"   - Removed {len(invalid_sales)} rows with invalid sales volumes")
    
    # Engine size should be reasonable (1.5-5.0L for BMW)
    invalid_engine = cleaned_df[(cleaned_df['Engine_Size_L'] < 1.5) | (cleaned_df['Engine_Size_L'] > 5.0)]
    if len(invalid_engine) > 0:
        cleaned_df = cleaned_df[(cleaned_df['Engine_Size_L'] >= 1.5) & (cleaned_df['Engine_Size_L'] <= 5.0)]
        validation_issues += len(invalid_engine)
        print(f"   - Removed {len(invalid_engine)} rows with invalid engine sizes")
    
    if validation_issues == 0:
        print("   - All data ranges are valid")
    
    # 7. Create derived features for analysis
    print("\n7. Creating derived features for analysis:")
    
    # Revenue (Price * Sales Volume)
    cleaned_df['Total_Revenue'] = cleaned_df['Price_USD'] * cleaned_df['Sales_Volume']
    print("   - Added 'Total_Revenue' column")
    
    # Price category
    price_bins = [0, 50000, 75000, 100000, float('inf')]
    price_labels = ['Budget', 'Mid-Range', 'Premium', 'Luxury']
    cleaned_df['Price_Category'] = pd.cut(cleaned_df['Price_USD'], bins=price_bins, labels=price_labels)
    print("   - Added 'Price_Category' column")
    
    # Model category (based on BMW model naming)
    def categorize_model(model):
        if 'i' in model.lower():
            return 'Electric/Hybrid'
        elif 'm' in model.lower():
            return 'Performance'
        elif 'x' in model.lower():
            return 'SUV'
        else:
            return 'Sedan'
    
    cleaned_df['Model_Category'] = cleaned_df['Model'].apply(categorize_model)
    print("   - Added 'Model_Category' column")
    
    # Age category for mileage
    mileage_bins = [0, 50000, 100000, 150000, float('inf')]
    mileage_labels = ['Low', 'Medium', 'High', 'Very High']
    cleaned_df['Mileage_Category'] = pd.cut(cleaned_df['Mileage_KM'], bins=mileage_bins, labels=mileage_labels)
    print("   - Added 'Mileage_Category' column")
    
    # 8. Sort data for consistency
    cleaned_df = cleaned_df.sort_values(['Year', 'Model', 'Region']).reset_index(drop=True)
    print("\n8. Sorted data by Year, Model, and Region")
    
    # 9. Final summary
    print("\n" + "="*70)
    print("CLEANING SUMMARY")
    print("="*70)
    print(f"Original rows: {initial_rows}")
    print(f"Final rows: {len(cleaned_df)}")
    print(f"Rows removed: {initial_rows - len(cleaned_df)} ({((initial_rows - len(cleaned_df))/initial_rows*100):.2f}%)")
    print(f"Final columns: {len(cleaned_df.columns)}")
    print(f"\nFinal data quality:")
    print(f"  - Missing values: {cleaned_df.isnull().sum().sum()}")
    print(f"  - Duplicate rows: {cleaned_df.duplicated().sum()}")
    print(f"  - Data types correct: [ok]")
    
    return cleaned_df


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
        
        # Clean and preprocess the data
        cleaned_data = clean_and_preprocess_data(bmw_data)
        
        # Save the cleaned data
        output_path = os.path.join("data-bmw", "BMW sales data (2020-2024) Cleaned.xlsx")
        try:
            cleaned_data.to_excel(output_path, index=False, engine='openpyxl')
            print(f"\n{'='*70}")
            print(f"✓ Cleaned data saved successfully to: {output_path}")
            print(f"{'='*70}")
            
            # Display sample of cleaned data
            print(f"\nSample of cleaned data (first 5 rows):")
            print(cleaned_data.head())
            
            print(f"\nCleaned data columns:")
            print(cleaned_data.columns.tolist())
            
            print(f"\nCleaned data statistics:")
            print(cleaned_data.describe())
            
        except Exception as e:
            print(f"\n✗ Error saving cleaned data: {str(e)}")

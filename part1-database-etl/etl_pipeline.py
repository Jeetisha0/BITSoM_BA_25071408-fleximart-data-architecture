# etl_pipeline.py
# Part 1: ETL Pipeline for FlexiMart
# Step 1: EXTRACT (Read raw CSV files safely)

import pandas as pd
import os

# -------------------------------
# Get correct base directory
# -------------------------------
# This file is inside: part1-database-etl/
# We move one level up to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")

CUSTOMERS_FILE = os.path.join(DATA_DIR, "customers_raw.csv")
PRODUCTS_FILE = os.path.join(DATA_DIR, "products_raw.csv")
SALES_FILE = os.path.join(DATA_DIR, "sales_raw.csv")


def extract_data():
    """Extract raw CSV files into pandas DataFrames"""
    try:
        customers_df = pd.read_csv(CUSTOMERS_FILE)
        products_df = pd.read_csv(PRODUCTS_FILE)
        sales_df = pd.read_csv(SALES_FILE)

        print("✅ Data extracted successfully")
        print(f"Customers records: {len(customers_df)}")
        print(f"Products records: {len(products_df)}")
        print(f"Sales records: {len(sales_df)}")

        return customers_df, products_df, sales_df

    except Exception as e:
        print("❌ Error during data extraction")
        print(e)
        return None, None, None


if __name__ == "__main__":
    extract_data()

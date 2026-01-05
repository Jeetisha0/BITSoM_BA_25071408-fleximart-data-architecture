# etl_pipeline.py
# Part 1: ETL Pipeline for FlexiMart
# Step 2: TRANSFORM - Clean Customers Data

import pandas as pd
import os
import re

# -------------------------------
# Setup paths safely
# -------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

CUSTOMERS_FILE = os.path.join(DATA_DIR, "customers_raw.csv")


def standardize_phone(phone):
    """Convert phone numbers to +91-XXXXXXXXXX format"""
    if pd.isna(phone):
        return None

    phone = str(phone).strip()

    # Remove all non-digit characters
    digits = re.sub(r"\D", "", phone)

    # Remove leading country code or zero
    if digits.startswith("91") and len(digits) > 10:
        digits = digits[-10:]
    elif digits.startswith("0") and len(digits) > 10:
        digits = digits[-10:]

    if len(digits) == 10:
        return f"+91-{digits}"

    return None


def clean_customers():
    print("🔹 Cleaning customers data...")

    df = pd.read_csv(CUSTOMERS_FILE)

    initial_count = len(df)

    # Trim spaces
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Drop duplicate customers
    df = df.drop_duplicates(subset=["customer_id"])

    duplicates_removed = initial_count - len(df)

    # Drop rows with missing email (email is NOT NULL)
    missing_emails = df["email"].isna().sum()
    df = df.dropna(subset=["email"])

    # Standardize phone numbers
    df["phone"] = df["phone"].apply(standardize_phone)

    # Standardize registration_date
    df["registration_date"] = pd.to_datetime(
        df["registration_date"], errors="coerce", dayfirst=True
    ).dt.strftime("%Y-%m-%d")

    print("✅ Customers cleaned successfully")
    print(f"Initial records: {initial_count}")
    print(f"Duplicates removed: {duplicates_removed}")
    print(f"Missing emails removed: {missing_emails}")
    print(f"Final records: {len(df)}")

    return df


if __name__ == "__main__":
    clean_customers()

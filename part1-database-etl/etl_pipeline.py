# etl_pipeline.py
# FlexiMart - Part 1 ETL Pipeline
# EXTRACT + TRANSFORM + DATA QUALITY REPORT

import pandas as pd
import os
import re

# -------------------------------
# PATH SETUP (SAFE & PORTABLE)
# -------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

CUSTOMERS_FILE = os.path.join(DATA_DIR, "customers_raw.csv")
PRODUCTS_FILE = os.path.join(DATA_DIR, "products_raw.csv")
SALES_FILE = os.path.join(DATA_DIR, "sales_raw.csv")

REPORT_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data_quality_report.txt"
)

# -------------------------------
# HELPER FUNCTIONS
# -------------------------------

def standardize_phone(phone):
    if pd.isna(phone):
        return None
    phone = str(phone).strip()
    digits = re.sub(r"\D", "", phone)

    if digits.startswith("91") and len(digits) > 10:
        digits = digits[-10:]
    elif digits.startswith("0") and len(digits) > 10:
        digits = digits[-10:]

    if len(digits) == 10:
        return f"+91-{digits}"

    return None


def standardize_category(category):
    if pd.isna(category):
        return None
    category = category.strip().lower()

    if category == "electronics":
        return "Electronics"
    elif category == "fashion":
        return "Fashion"
    elif category == "groceries":
        return "Groceries"
    return category.title()


# -------------------------------
# CUSTOMERS TRANSFORM
# -------------------------------

def clean_customers():
    print("🔹 Cleaning customers data...")
    df = pd.read_csv(CUSTOMERS_FILE)

    initial_count = len(df)

    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df = df.drop_duplicates(subset=["customer_id"])
    duplicates_removed = initial_count - len(df)

    missing_emails = df["email"].isna().sum()
    df = df.dropna(subset=["email"])

    df["phone"] = df["phone"].apply(standardize_phone)

    df["registration_date"] = pd.to_datetime(
        df["registration_date"], errors="coerce", dayfirst=True
    ).dt.strftime("%Y-%m-%d")

    print(f"Final customer records: {len(df)}")

    report = {
        "file": "customers_raw.csv",
        "initial": initial_count,
        "duplicates_removed": duplicates_removed,
        "missing_values_handled": missing_emails,
        "final": len(df)
    }

    return df, report


# -------------------------------
# PRODUCTS TRANSFORM
# -------------------------------

def clean_products():
    print("\n🔹 Cleaning products data...")
    df = pd.read_csv(PRODUCTS_FILE)

    initial_count = len(df)

    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    missing_prices = df["price"].isna().sum()
    df = df.dropna(subset=["price"])

    missing_stock = df["stock_quantity"].isna().sum()
    df["stock_quantity"] = df["stock_quantity"].fillna(0).astype(int)

    df["category"] = df["category"].apply(standardize_category)

    print(f"Final product records: {len(df)}")

    report = {
        "file": "products_raw.csv",
        "initial": initial_count,
        "duplicates_removed": 0,
        "missing_values_handled": missing_prices + missing_stock,
        "final": len(df)
    }

    return df, report


# -------------------------------
# SALES TRANSFORM
# -------------------------------

def clean_sales():
    print("\n🔹 Cleaning sales data...")
    df = pd.read_csv(SALES_FILE)

    initial_count = len(df)

    df = df.drop_duplicates(subset=["transaction_id"])
    duplicates_removed = initial_count - len(df)

    missing_customer = df["customer_id"].isna().sum()
    missing_product = df["product_id"].isna().sum()

    df = df.dropna(subset=["customer_id", "product_id"])

    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"], errors="coerce", dayfirst=True
    ).dt.strftime("%Y-%m-%d")

    print(f"Final sales records: {len(df)}")

    report = {
        "file": "sales_raw.csv",
        "initial": initial_count,
        "duplicates_removed": duplicates_removed,
        "missing_values_handled": missing_customer + missing_product,
        "final": len(df)
    }

    return df, report


# -------------------------------
# MAIN EXECUTION
# -------------------------------

if __name__ == "__main__":
    customers_df, cust_report = clean_customers()
    products_df, prod_report = clean_products()
    sales_df, sales_report = clean_sales()

    with open(REPORT_FILE, "w") as f:
        f.write("FlexiMart Data Quality Report\n")
        f.write("=" * 35 + "\n\n")

        for r in [cust_report, prod_report, sales_report]:
            f.write(f"File: {r['file']}\n")
            f.write(f"Records processed: {r['initial']}\n")
            f.write(f"Duplicates removed: {r.get('duplicates_removed', 0)}\n")
            f.write(f"Missing values handled: {r.get('missing_values_handled', 0)}\n")
            f.write(f"Records loaded: {r['final']}\n\n")

    print("\n📄 Data quality report generated successfully")

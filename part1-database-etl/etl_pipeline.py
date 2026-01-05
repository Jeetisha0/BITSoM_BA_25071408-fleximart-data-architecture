# etl_pipeline.py
# FlexiMart – Part 1 ETL Pipeline (FINAL CLEAN VERSION)

import pandas as pd
import os
import re
import mysql.connector

# -------------------------------
# GLOBAL ID MAPS
# -------------------------------
CUSTOMER_ID_MAP = {}
PRODUCT_ID_MAP = {}

# -------------------------------
# MYSQL DATABASE CONFIG
# -------------------------------
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Jeet@079",
    "database": "fleximart"
}

# -------------------------------
# PATH SETUP
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
    digits = re.sub(r"\D", "", str(phone))

    if digits.startswith("91") and len(digits) > 10:
        digits = digits[-10:]
    elif digits.startswith("0") and len(digits) > 10:
        digits = digits[-10:]

    return f"+91-{digits}" if len(digits) == 10 else None


def standardize_category(category):
    if pd.isna(category):
        return None
    category = category.strip().lower()

    if category == "electronics":
        return "Electronics"
    if category == "fashion":
        return "Fashion"
    if category == "groceries":
        return "Groceries"

    return category.title()

# -------------------------------
# CLEAN CUSTOMERS
# -------------------------------
def clean_customers():
    print("Cleaning customers data...")
    df = pd.read_csv(CUSTOMERS_FILE)
    initial = len(df)

    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df = df.drop_duplicates(subset=["customer_id"])
    duplicates = initial - len(df)

    missing_emails = df["email"].isna().sum()
    df = df.dropna(subset=["email"])

    df["phone"] = df["phone"].apply(standardize_phone)

    df["registration_date"] = pd.to_datetime(
        df["registration_date"], errors="coerce", dayfirst=True
    ).dt.strftime("%Y-%m-%d")

    print(f"Final customer records: {len(df)}")

    return df, {
        "file": "customers_raw.csv",
        "initial": initial,
        "duplicates_removed": duplicates,
        "missing_values_handled": missing_emails,
        "final": len(df)
    }

# -------------------------------
# CLEAN PRODUCTS
# -------------------------------
def clean_products():
    print("Cleaning products data...")
    df = pd.read_csv(PRODUCTS_FILE)
    initial = len(df)

    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    missing_prices = df["price"].isna().sum()
    df = df.dropna(subset=["price"])

    missing_stock = df["stock_quantity"].isna().sum()
    df["stock_quantity"] = df["stock_quantity"].fillna(0).astype(int)

    df["category"] = df["category"].apply(standardize_category)

    print(f"Final product records: {len(df)}")

    return df, {
        "file": "products_raw.csv",
        "initial": initial,
        "duplicates_removed": 0,
        "missing_values_handled": missing_prices + missing_stock,
        "final": len(df)
    }

# -------------------------------
# CLEAN SALES
# -------------------------------
def clean_sales():
    print("Cleaning sales data...")
    df = pd.read_csv(SALES_FILE)
    initial = len(df)

    df = df.drop_duplicates(subset=["transaction_id"])
    duplicates = initial - len(df)

    missing_ids = df["customer_id"].isna().sum() + df["product_id"].isna().sum()
    df = df.dropna(subset=["customer_id", "product_id"])

    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"], errors="coerce", dayfirst=True
    ).dt.strftime("%Y-%m-%d")

    print(f"Final sales records: {len(df)}")

    return df, {
        "file": "sales_raw.csv",
        "initial": initial,
        "duplicates_removed": duplicates,
        "missing_values_handled": missing_ids,
        "final": len(df)
    }

# -------------------------------
# CLEAR TABLES
# -------------------------------
def clear_tables():
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("SET FOREIGN_KEY_CHECKS = 0")
    cur.execute("TRUNCATE TABLE order_items")
    cur.execute("TRUNCATE TABLE orders")
    cur.execute("TRUNCATE TABLE customers")
    cur.execute("TRUNCATE TABLE products")
    cur.execute("SET FOREIGN_KEY_CHECKS = 1")

    conn.commit()
    cur.close()
    conn.close()

    print(" Existing tables cleared")

# -------------------------------
# LOAD CUSTOMERS
# -------------------------------
def load_customers(df):
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()

    sql = """
    INSERT INTO customers
    (first_name, last_name, email, phone, city, registration_date)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    for _, row in df.iterrows():
        cur.execute(sql, (
            row["first_name"],
            row["last_name"],
            row["email"],
            row["phone"],
            row["city"],
            row["registration_date"]
        ))
        CUSTOMER_ID_MAP[row["customer_id"]] = cur.lastrowid

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Customers loaded")

# -------------------------------
# LOAD PRODUCTS
# -------------------------------
def load_products(df):
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()

    sql = """
    INSERT INTO products
    (product_name, category, price, stock_quantity)
    VALUES (%s, %s, %s, %s)
    """

    for _, row in df.iterrows():
        cur.execute(sql, (
            row["product_name"],
            row["category"],
            float(row["price"]),
            int(row["stock_quantity"])
        ))
        PRODUCT_ID_MAP[row["product_id"]] = cur.lastrowid

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Products loaded")

# -------------------------------
# LOAD ORDERS + ITEMS
# -------------------------------
def load_orders_and_items(df):
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()

    order_sql = """
    INSERT INTO orders (customer_id, order_date, total_amount, status)
    VALUES (%s, %s, %s, %s)
    """

    item_sql = """
    INSERT INTO order_items
    (order_id, product_id, quantity, unit_price, subtotal)
    VALUES (%s, %s, %s, %s, %s)
    """

    for _, row in df.iterrows():

    # Skip invalid numeric values
    if pd.isna(row["quantity"]) or pd.isna(row["unit_price"]):
        continue

    if row["customer_id"] not in CUSTOMER_ID_MAP:
        continue

    if row["product_id"] not in PRODUCT_ID_MAP:
        continue

    total = float(row["quantity"] * row["unit_price"])
    
        cur.execute(order_sql, (
            CUSTOMER_ID_MAP[row["customer_id"]],
            row["transaction_date"],
            total,
            row["status"]
        ))

        order_id = cur.lastrowid

        cur.execute(item_sql, (
            order_id,
            PRODUCT_ID_MAP[row["product_id"]],
            int(row["quantity"]),
            float(row["unit_price"]),
            total
        ))

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Orders & order_items loaded")

# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    customers_df, c_rep = clean_customers()
    products_df, p_rep = clean_products()
    sales_df, s_rep = clean_sales()

    clear_tables()
    load_customers(customers_df)
    load_products(products_df)
    load_orders_and_items(sales_df)

    with open(REPORT_FILE, "w") as f:
        for r in [c_rep, p_rep, s_rep]:
            f.write(str(r) + "\n")

    print("\n ETL PIPELINE COMPLETED SUCCESSFULLY")

# Star Schema Design for FlexiMart Data Warehouse

## Section 1: Schema Overview

### FACT TABLE: fact_sales
**Grain:** One row per product per order line item  
**Business Process:** Sales transactions

**Measures (Numeric Facts):**
- quantity_sold: Number of units sold
- unit_price: Price per unit at time of sale
- discount_amount: Discount applied on the product
- total_amount: Final amount calculated as (quantity × unit_price − discount)

**Foreign Keys:**
- date_key → dim_date
- product_key → dim_product
- customer_key → dim_customer


### DIMENSION TABLE: dim_date
**Purpose:** Date dimension for time-based analysis  
**Type:** Conformed dimension

**Attributes:**
- date_key (PK): Surrogate key in YYYYMMDD format
- full_date: Actual calendar date
- day_of_week: Day name (Monday, Tuesday, etc.)
- month: Month number (1–12)
- month_name: Name of the month
- quarter: Quarter of the year (Q1, Q2, Q3, Q4)
- year: Calendar year
- is_weekend: Boolean indicating weekend or weekday


### DIMENSION TABLE: dim_product
**Purpose:** Stores descriptive information about products

**Attributes:**
- product_key (PK): Surrogate key
- product_id: Business product identifier
- product_name: Name of the product
- category: Product category
- subcategory: Product subcategory
- unit_price: Standard price of the product


### DIMENSION TABLE: dim_customer
**Purpose:** Stores descriptive information about customers

**Attributes:**
- customer_key (PK): Surrogate key
- customer_id: Business customer identifier
- customer_name: Full name of the customer
- city: City of residence
- state: State of residence
- customer_segment: Customer value segment


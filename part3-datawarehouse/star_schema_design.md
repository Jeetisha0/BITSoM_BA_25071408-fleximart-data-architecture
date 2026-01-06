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

## Section 2: Design Decisions 
- The data warehouse is designed at the transaction line-item level to capture the most detailed view of sales activity. This granularity allows analysis at the product, customer, and date level and supports accurate aggregation for reporting. It enables flexibility to drill down from summary reports to individual product-level transactions.

- Surrogate keys are used instead of natural keys to ensure consistency and stability within the data warehouse. Business identifiers such as customer_id or product_id may change in source systems, but surrogate keys remain constant, preventing data integrity issues and improving join performance.

- The star schema design supports drill-down and roll-up operations by separating numeric measures from descriptive attributes. Analysts can easily roll up data by month, quarter, or year, and drill down to specific dates, products, or customers. This structure simplifies analytical queries and improves performance for business intelligence use cases.

## Section 3: Sample Data Flow

**Source Transaction:**  
Order #101, Customer “John Doe”, Product “Laptop”, Qty: 2, Price: 50000

**Becomes in Data Warehouse:**

**fact_sales**
- date_key: 20240115  
- product_key: 5  
- customer_key: 12  
- quantity_sold: 2  
- unit_price: 50000  
- total_amount: 100000  

**dim_date**
- date_key: 20240115  
- full_date: 2024-01-15  
- month: 1  
- quarter: Q1  

**dim_product**
- product_key: 5  
- product_name: Laptop  
- category: Electronics  

**dim_customer**
- customer_key: 12  
- customer_name: John Doe  
- city: Mumbai  

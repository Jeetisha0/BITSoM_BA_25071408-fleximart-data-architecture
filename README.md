# BITSoM_BA_25071408-fleximart-data-architecture
**FlexiMart Data Architecture Project**

Student Name: Jeetisha Khotele
Student ID: BITSoM_BA_25071408
Email: jeetishakhotele@gmail.com

Date: 6 Jan 2026

### Project Overview

This project demonstrates the end-to-end design and implementation of a data architecture solution for FlexiMart.
It covers the complete journey from raw CSV files to clean relational data, flexible NoSQL storage, and a data warehouse built for analytics. The solution supports both operational reporting and business-level insights.

### Project Highlights

- Built a fully automated ETL pipeline to clean and load raw data into MySQL
- Designed a normalized relational database for transactional data
- Implemented business-focused SQL queries for reporting and analysis
- Evaluated and implemented MongoDB for handling flexible product attributes
- Designed a star schema data warehouse for historical and analytical reporting
- Created OLAP queries to support management and strategic decisions
- Maintained a clean GitHub repository structure with proper documentation

### Repository Structure
├── data/
│   ├── customers_raw.csv
│   ├── products_raw.csv
│   └── sales_raw.csv
│
├── part1-database-etl/
│   ├── README.md
│   ├── etl_pipeline.py
│   ├── business_queries.sql
│   ├── schema_documentation.md
│   ├── data_quality_report.txt
│   └── requirements.txt
│
├── part2-nosql/
│   ├── README.md
│   ├── nosql_analysis.md
│   ├── mongodb_operations.js
│   └── products_catalog.json
│
├── part3-datawarehouse/
│   ├── README.md
│   ├── star_schema_design.md
│   ├── warehouse_schema.sql
│   ├── warehouse_data.sql
│   └── analytics_queries.sql
│
├── .gitignore
└── README.md

### Technologies Used

Python 3.x (pandas, mysql-connector-python)

MySQL 8.0 (relational database & data warehouse)

MongoDB 6.0 (NoSQL document database)

GitHub & GitHub Desktop (version control and collaboration)

### Setup Instructions
**Database Setup**

**Create the required databases:**
fleximart (Part 1 – ETL & relational database)
fleximart_dw (Part 3 – Data warehouse)

**Run the ETL pipeline:**

python part1-database-etl/etl_pipeline.py

**Execute business queries:**

mysql -u root -p fleximart < part1-database-etl/business_queries.sql

**Set up the data warehouse:**

mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql

**MongoDB Setup**

Run the MongoDB operations script:
mongosh < part2-nosql/mongodb_operations.js

**Key Learnings**

- Designed and implemented a complete ETL pipeline with data quality handling
- Gained hands-on experience with relational vs NoSQL database design
- Learned dimensional modeling using a star schema
- Developed analytical and OLAP queries for business reporting
- Improved understanding of data architecture best practices

**Challenges Faced**

- Handling inconsistent and missing data: Resolved through cleaning, deduplication, standardization, and validation during ETL
- Mapping transactional data into a dimensional model: Solved using surrogate keys and clearly defined fact–dimension relationships
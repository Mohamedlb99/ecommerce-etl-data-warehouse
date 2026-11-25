# E-commerce ETL & Data Warehouse Project

## Project Overview

This project implements an ETL pipeline for an e-commerce business.

It extracts data from CSV files, cleans and transforms the data using Python and Pandas, and loads the processed data into SQL Server.

The project also includes a Star Schema Data Warehouse design to support data analysis and reporting.

## Technologies Used

- Python
- Pandas
- SQL Server
- SQLAlchemy
- PyODBC
- VS Code

## Project Structure

ecommerce_etl_project/
│
├── DATA/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── order_items.csv
│   └── cleaned/
│
├── LOGS/
│   ├── LOAD.LOG
│   └── Ecommerce_ETL.LOG
│
├── SCRIPTS/
│   ├── extract.py
│   ├── Cleaning.py
│   ├── validation.py
│   ├── profiling.py
│   └── load.py
│
├── SQL/
│   └── create_tables.sql
├── LOGS/
│   ├── LOAD.LOG
│   └── Ecommerce_ETL.LOG
│
├── images/
│   └── data_warehouse_schema.jpg
│
└── README.md

## ETL Process

### 1. Extract
Extracted data from CSV files using Python and Pandas.

### 2. Transform
- Cleaned missing and invalid values.
- Removed duplicate records.
- Validated data quality.
- Merged orders with order items.
- Calculated net sales after discounts.

### 3. Load
Loaded the transformed data into SQL Server using SQLAlchemy and Pandas.

Implemented incremental loading to avoid duplicate records.

## Data Warehouse Design

The Data Warehouse uses a Star Schema design.

It contains three tables:

- DimCustomers: Stores customer information.
- DimProducts: Stores product information.
- FactSales: Stores sales transaction details.

FactSales is connected to DimCustomers and DimProducts using Foreign Keys.

## Data Validation

Implemented data quality checks to ensure:

- No duplicate primary keys.
- Valid customer and product references.
- Valid data types.
- Discount values do not exceed 90%.
- Required fields are not missing.

## Logging

Implemented logging to track ETL pipeline execution.

- Recorded successful data loading operations.
- Captured errors during the ETL process.
- Stored log messages in log files for monitoring and troubleshooting.


## How to Run

1. Install the required Python libraries.
2. Configure the SQL Server connection in load.py.
3. Make sure the Data Warehouse database and tables exist.
4. Run the ETL scripts in the correct order.
5. Execute load.py to load the processed data into SQL Server.




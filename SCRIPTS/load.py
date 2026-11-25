import pandas as pd
import pyodbc
import logging
from sqlalchemy import create_engine
from urllib.parse import quote_plus

logging.basicConfig(
      filename='ecommerce_etl_project/logs/load.log',
      filemode='w',
      level=logging.INFO,
      format="%(asctime)s - %(message)s - %(levelname)s "

)

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=PERCY\\SQLEXPRESS;"
    "DATABASE=EcommerceDWH;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

params = quote_plus(connection_string)
engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={params}"
)

with engine.connect() as conn:
    logging.info("Connected successfully")

df_customers = pd.read_csv(
    "ecommerce_etl_project/DATA/cleaned/customers_cleaned.csv")

df_sql_customers = pd.read_sql(
    "SELECT customer_id FROM gold.DimCustomers",
    con=engine
) 


df_new_customers = df_customers[~df_customers["customer_id"].isin(df_sql_customers["customer_id"])]    

print(len(df_sql_customers))
print(len(df_new_customers))

try:
    df_new_customers.to_sql(
        name='DimCustomers',
        con=engine,
        schema='gold',
        if_exists='append',
        index=False
    )
    logging.info("Customers loaded successfully")

except Exception as e:
        logging.error(f"Customers loading failed: {e}")   

df_products = pd.read_csv(
    "ecommerce_etl_project/DATA/cleaned/products_cleaned.csv",
)

df_sql_products = pd.read_sql(
     "SELECT product_id FROM gold.Dimproducts",
     con= engine
)

df_new_products = df_products[~df_products["product_id"].isin(df_sql_products["product_id"])]

try:
    df_new_products.to_sql(
        name='DimProducts',
        con=engine,
        schema='gold',
        if_exists='append',
        index=False
    )
    logging.info("Products loaded successfully")

except Exception as e:
        logging.error(f"Products loading failed: {e}")

### FactSales table 

df_orders = pd.read_csv(
      "ecommerce_etl_project/DATA/cleaned/orders_cleaned.csv"
)        

df_orders_items = pd.read_csv(
      "ecommerce_etl_project/DATA/cleaned/order_items_cleaned.csv"
) 

df_sales = pd.merge(
    df_orders_items,
    df_orders,
    on= "order_id",
    how="left"
)
df_sales["net_sales"] = df_sales["quantity"] * df_sales["unit_price"] * (1 - (df_sales["discount_pct"]/100))

df_sql_sales = pd.read_sql(
     "SELECT order_item_id FROM gold.FactSales",
     con=engine
)

df_new_sales = df_sales[~df_sales["order_item_id"].isin(df_sql_sales["order_item_id"])]

try:
    df_new_sales.to_sql(
        name = "FactSales",
        con= engine,
        schema = "gold",
        if_exists= "append",
        index= False
    )
    logging.info("factsales loaded successfully to sql server")
except Exception as e:
    logging.error("df_new_sales load fail error %s", e)    






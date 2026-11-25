CREATE DATABASE EcommerceDWH;
use EcommerceDWH;
--  CREATE SCHEMA gold;
/*CREATE TABLE  gold.DimCustomers(
customer_id INT NOT NULL,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(50)  NULL,
city VARCHAR(50) NOT NULL,
country VARCHAR(20) NOT NULL,
signup_date date not null,
CONSTRAINT PK_DimCustomers PRIMARY KEY (customer_id))*/

-- to see schema name and tables
/*SELECT TABLE_SCHEMA, TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME = 'DimCustomers';*/

-- DimProduct table 
/*CREATE TABLE gold.products(
product_id INT NOT NULL,
product_name VARCHAR(50) NOT NULL,
category  VARCHAR(50) NOT NULL,
unit_price INT NOT NULL,
is_acive char not null,
constraint PK_DimProducts PRIMARY KEY (product_id)
);*/

-- to rename table name
--EXEC sp_rename 'gold.products', 'DimProducts';

/* to change data type
alter table gold.DimProducts
alter column unit_price DECIMAL(10,2) NOT NULL
*/

/* rename column name
EXEC sp_rename
'gold.DimProducts.is_acive',
'is_active',
'COLUMN' */
/*
CREATE TABLE gold.FactSales(
order_item_id INT NOT NULL,
order_id INT NOT NULL,
order_date date NOT NULL,
customer_id INT NOT NULL,
product_id INT NOT NULL,
payment_method VARCHAR(20) NOT NULL,
order_status VARCHAR(20) NOT NULL,
quantity INT NOT NULL,
unit_price DECIMAL(10,2) NOT NULL,
discount_pct DECIMAL(5,2) NOT NULL,
net_sales DECIMAL(10,2) NOT NULL,
CONSTRAINT FactSales_pk primary key (order_item_id),
CONSTRAINT FactSales_Fk1 FOREIGN KEY (customer_id) REFERENCES gold.DimCustomers(customer_id),
CONSTRAINT FactSales_Fk2 FOREIGN KEY (product_id) REFERENCES gold.DimProducts(product_id)
) */
import pandas as pd
import logging
import Cleaning ,profiling 
import validation as vd

# Create log file
logging.basicConfig(
    filename='ecommerce_etl_project/logs/ecommerce_etl.log',
    filemode='w',
    level=logging.INFO,
    format="%(asctime)s - %(message)s - %(levelname)s "
)

#############
# 1- Extract customers file
############

df =pd.read_csv(r'ecommerce_etl_project/DATA/customers.csv')
logging.info("Customers: data extracted successfully")

# Create copy of dataframe
customers = df.copy()
#-----------------
# 1- profiling data
#-----------------

# check spaces after and before string columns
check_space = ["first_name", "last_name", "city"]
check_space_before = profiling.profile_space_strings(customers,check_space)
logging.info("Customers: check_space_before is %s", check_space_before)


# check spaces , empty, nan values in df
tot_nan , empty_str, total_space = profiling.profile_empty(customers, check_space)
logging.info("Customers: Missing values: %s", tot_nan)
logging.info("Customers: Empty strings: %s", empty_str)
logging.info("Customers: Whitespace only: %s", total_space)

# -------------------------
# 2. Cleaning
# -------------------------


# clean the string columns from spaces
customers = Cleaning.white_space(customers, check_space)
logging.info("Customers: white space after and before any string value cleaned")

#change date column to date type
Cleaning.date(customers, "signup_date")
logging.info("Customers: Signup date dtype: %s", customers["signup_date"].dtype)
logging.info("Customers: Invalid dates (NaT): %s", customers["signup_date"].isna().sum())

# -------------------------
# 3. Validation
# -------------------------

# check validation of spaces after cleaning
validate_White_space = vd.validate_white_space(customers, check_space)
logging.info(f"Customers: validate_White_space after cleaning is {validate_White_space}")


# check validate of datetime type:
valide_date_type = vd.check_date_time_validate(customers,"signup_date")
logging.info("Customers: date columns type validate is %s", valide_date_type)

# Check Validate of column Unique
Primary_key_check = vd.check_unique(customers,"customer_id")
logging.info("Customers: customer_id column %s to be primary key", Primary_key_check)

# Check Validate of full columns Duplication 
columns_unique  = ["first_name","last_name", "email", "city","country","signup_date"]
state_Duplicate_Customer = vd.check_full_duplication(customers, columns_unique)
logging.info("Customers: Duplication state %s", state_Duplicate_Customer)
if state_Duplicate_Customer:
    ## remove only full duplication 
    customers = Cleaning.remove_duplication(customers, columns_unique)
    logging.info("Customers: rows removed which have full duplication")

####
## save customers file after cleanining
####
customers.to_csv(
    "ecommerce_etl_project/DATA/cleaned/customers_cleaned.csv",
    index=False
)
logging.info("Customers: Customer file saved after cleaned ")

#######
# 2- products csv file
#######
df_1 = pd.read_csv("ecommerce_etl_project/DATA/products.csv")
logging.info("products data extracted successfully")
##copy of dataframe
products = df_1.copy()

# #-----------------
# # 1- profiling data
# #-----------------
## check spaces in string values which contain a string
string_columns = ["product_name","category", "is_active"]
chk_spaces_1 = profiling.profile_space_strings(products,string_columns)
logging.info("products: check spaces in product file %s", chk_spaces_1)

## check empty values, total spaces, ""
tot_nan_1,empty_1, spaces_1 = profiling.profile_empty(products,string_columns)
logging.info("products: Missing values: %s", tot_nan_1)
logging.info("products: empty values: %s", empty_1)
logging.info("products: spaces values: %s", spaces_1)


##############
## Validation 
##############

## check validation of unique primary key
primary_key_chk1 = vd.check_unique(products,"product_id")
logging.info("products: product_id column %s to be primary key",primary_key_chk1)


## Check all values are Positive in unite price

unit_price_state = vd.check_number_values(products, "unit_price")
if unit_price_state:
    message = "All prices are positive"
else:
    message = "Invalid prices found"

logging.info("Products: unit_price validation: %s", message)

## check all values in is_active colume between 'Y' or 'N'
values = ['Y', 'N']
is_active_values = vd.check_boolen(products, "is_active", values)
if is_active_values:
    message1 = "All values in (Y / N)"
else:
    message1 = "have error values"

logging.info("Products: is_active columns validation: %s", message1)

###
# save products cleaned as excel
###

products.to_csv(
    "ecommerce_etl_project/DATA/cleaned/products_cleaned.csv",
    index= False
)
logging.info("Products: Product file saved after cleaned ")
########
### ORDERS FILE
########

df_2 = pd.read_csv(r'ecommerce_etl_project/DATA/orders.csv')

orders = df_2.copy()


######
## Profiling
######

# Check spaces in string,totalspces, empyt values(NAN), ''
orders_string_col = ["order_status","payment_method"]
chk_space_instrin_state = profiling.profile_space_strings(orders,orders_string_col)
logging.info("Orders: check spaces in orders file %s", chk_space_instrin_state)

# Check totalspces, empyt values(NAN), ''
tot_nan_orders,empty_orders, spaces_orders = profiling.profile_empty(orders,orders_string_col)
logging.info("orders: Missing values: %s", tot_nan_orders)
logging.info("orders: empty values: %s", empty_orders)
logging.info("orders: spaces values: %s", spaces_orders)

#

#######
### cleaning
#######
Cleaning.date(orders,"order_date")
#######
### validation
#######
# check validate_datetime_type
valide_date_type1 = vd.check_date_time_validate(orders,"order_date")
logging.info("orders: date columns type validate is %s", valide_date_type1)

# Check values in payment_method Between (CASH, Card, Wallet)
values = ['Cash', 'Wallet', 'Card']
Cash_method_values = vd.check_boolen(orders, "payment_method", values)
if Cash_method_values:
    message2 = "All values in (cash/card/wallet)"
else:
    message2 = "have error values"

logging.info("orders: Cash Method columns validation: %s", message2)

# Check values in order_status Between (Completed, Shipped, Cancelled, Pending)
values_1 = ["Completed", "Shipped", "Cancelled", "Pending"]
order_status_values = vd.check_boolen(orders, "order_status", values_1)
if Cash_method_values:
    message2 = "All values in (Completed, Shipped, Cancelled, Pending))"
else:
    message2 = "have error values"

logging.info("orders: order_status columns validation: %s", message2)
#check unique values
# check primary key column order_id
primary_key_chk2 = vd.check_unique(orders, "order_id")
logging.info("orders: order_id column %s to be primary key",primary_key_chk2)

# Check total duplication
duplicate_columns_chk = ["order_status","customer_id","payment_method","order_date"]
full_dublication_status = vd.check_full_duplication(orders,duplicate_columns_chk)
logging.info("orders: Duplication state %s", full_dublication_status)
if full_dublication_status:
    Cleaning.remove_duplication(orders,duplicate_columns_chk)
    logging.info("Orders: all rows which duplicated in all values except Order_id")

###Foreign Key Validation customer_id in customers_cleaned. csv
if not state_Duplicate_Customer :
    primary_key_customers = customers["customer_id"]
    Foreign_key_orders = orders["customer_id"]
    chk_keys_intow_tables = vd.chk_foreign_key(Foreign_key_orders,primary_key_customers)
    if chk_keys_intow_tables:
        logging.info("orders: all foreign keys are primary keys in other table")
    else:
        logging.error("Forders: foreign key validation failed: customer_id")
    
else:
    df_reference = pd.read_csv("ecommerce_etl_project/DATA/cleaned/customers_cleaned.csv",
                               usecols=["customer_id"])
        
    primary_key_customers = df_reference["customer_id"]
    Foreign_key_orders = orders["customer_id"]
    chk_keys_intow_tables = vd.chk_foreign_key(Foreign_key_orders,primary_key_customers)
    if chk_keys_intow_tables:
        logging.info("orders: all foreign keys are primary keys in other table")
    else:
        logging.error("orders: Foreign key validation failed: customer_id")    

#######
# save orders file after cleaning 
# #####        
orders.to_csv(
   "ecommerce_etl_project/DATA/cleaned/orders_cleaned.csv",
   index= False
)
logging.info("Orders: orders file saved after cleaned")

#########
## extract order items file
#########

df_3 = pd.read_csv("ecommerce_etl_project/DATA/order_items.csv")
order_items = df_3.copy()

logging.info("Order_items: loading file is successful")

######
# profiling
######
# check empty, and nan values in all file

chk_empty_values_state = profiling.chk_empty_nan(order_items)
logging.info("order_items: status of nan values %s", chk_empty_values_state)

######
## validation
######
## check negative and 0 values in quantity, unit_price
chk_quantity_values = vd.check_number_values(order_items, "quantity")
logging.info("order_items: quantity columns are %s values > 0",chk_quantity_values)

chk_unit_price_values = vd.check_number_values(order_items, "unit_price")
logging.info("order_items: chk_unit_price_values columns are %s values > 0",chk_unit_price_values)
### deal with data rejected in order_items
if (not chk_quantity_values) or (not chk_unit_price_values):
    df_items_rejectd = order_items.iloc[0:0].copy()
    df_items_rejectd = pd.concat([df_items_rejectd,order_items.loc[(order_items["quantity"] <= 0) | (order_items["unit_price"] <= 0)]])
    logging.info("order_items: some data have problem on its values (quantity , unit_price) columns will saved in order_items_rejected(csv)")
    order_items = order_items.drop(order_items.loc[(order_items["quantity"] <= 0) | (order_items["unit_price"] <= 0)].index)

######### 
### check full dublication
#########
full_duplication_state = vd.check_full_duplication(order_items,order_items.columns)

if full_duplication_state:
    Cleaning.remove_duplication(order_items,order_items.columns) 
    logging.info("order_items: all duplicated values are removed") 
else:
    logging.info("Order_items: no duplicated rows founded")
##########
### check primary key unique order_items_id
#########      
chk_order_items_pk = vd.check_unique(order_items,"order_item_id")
logging.info("order_items: order_items_id column %s to be primary key",chk_order_items_pk)

#######
## check all foreign keys order_id, product_id
order_items_fk1 = order_items["order_id"]
order_pk = orders["order_id"]
order_items_fk2 = order_items["product_id"]
product_pk = products["product_id"]

chk_fk1 = vd.chk_foreign_key(order_items_fk1,order_pk)
chk_fk2 = vd.chk_foreign_key(order_items_fk2,product_pk)

if chk_fk1:
    logging.info("order_items: order_id foreign keys are primary keys in other orders table")
else:
    logging.error("order_items: Foreign key validation failed: order_id") 
if chk_fk2:
    logging.info("order_items: product_id foreign keys are primary keys in other products table")
else:
    logging.error("order_items: Foreign key validation failed: product_id")  
##### move rows which effected to   df_items_rejectd   
    df_items_rejectd = pd.concat([df_items_rejectd ,order_items.loc[(~order_items_fk2.isin(product_pk))]])
### drop the rejected data from order_items    
    order_items =  order_items.drop(order_items.loc[~(order_items_fk2.isin(product_pk))].index)  
#### check again chk_fk2
    order_items_fk2 = order_items["product_id"]
    chk_fk2 = vd.chk_foreign_key(order_items_fk2,product_pk)

    if chk_fk2:
        logging.info("order_items: product_id foreign keys are primary keys in other products table")
    else:
        logging.error("order_items: Foreign key validation failed: product_id") 

###########
# ## CHECK VALUES IN DISCOUNT COLUMN >0 AND < 100
dicount_values = range(0, 91)

chk_order_items_discount = vd.check_boolen(order_items,"discount_pct",dicount_values) 
if chk_order_items_discount : 
    logging.info("Order_items: is in range 0- 90 in discount percent range") 
else:
    logging.info("Order_items: isnot in range 0- 90 in discount percent range") 
    df_items_rejectd = pd.concat([df_items_rejectd,order_items.loc[~(order_items["discount_pct"].isin(dicount_values))]])      
    order_items = order_items.drop((order_items.loc[~(order_items["discount_pct"].isin(dicount_values))]).index)
    logging.info("Order_items: has isolate the rows which not in range 0- 90 in discount percent range")

## re check chk_order_items_discount
chk_order_items_discount = vd.check_boolen(order_items,"discount_pct",dicount_values) 
if chk_order_items_discount : 
    logging.info("Order_items: after 2nd check discount percent range in range 0- 90")
else:
    logging.info("Order_items: after check 2nd time still have prob in range 0- 90 in discount percent range")
 
order_items.to_csv(
    "ecommerce_etl_project/DATA/cleaned/order_items_cleaned.csv"
    ,
    index=False
)
logging.info("order_items_cleaned saved successfully")
df_items_rejectd.to_csv(
    "ecommerce_etl_project/DATA/cleaned/orders_items_rejected.csv"
    ,
     index=False
)
logging.info("order_items_rejected saved successfully")
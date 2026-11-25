import pandas as pd
## check validate_White_ spaces in string

def validate_white_space(df, cols):
    total_error = 0
    for col in cols:
        for item in df[col]:
            checkBeforeStrip = len(item)
            CheckAfterStrip = len(item.strip())
            if (checkBeforeStrip -CheckAfterStrip) > 0:
                 total_error += 1
                 break     
    if   total_error > 0:
        return False
    else:
        return True       
## check validate_datetime_type
def check_date_time_validate(df, col):
    if   pd.api.types.is_datetime64_any_dtype(df[col]):
        return True
    else:
        return False
### check unique columns 
def check_unique(df, col):
    duplicate = df[col].duplicated().sum()
    nan_value = df[col].isna().sum()
    if (duplicate == 0 and nan_value == 0):
        return True
    else:
        return False  

### check full duplication

def check_full_duplication(df, col):
    return df.duplicated(subset = col, keep = False).any()

### check number values postive > 0 or negative

def check_number_values(df, col):
    if (df[col] > 0).all():
        return True
    else:
        return False

#### check value  in Values

def check_boolen(df, col, Value):
    if df[col].isin(Value).all():
        return True
    else:
        return False

## check foreign_key:
def chk_foreign_key(fcol,pcol):
    if fcol.isin(pcol).all():
        return True
    else:
        return False 

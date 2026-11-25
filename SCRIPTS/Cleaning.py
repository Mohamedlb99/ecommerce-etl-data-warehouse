import pandas as pd
#clean white space
def white_space (df,cols):
    for col in cols:
        df[col] = df[col].str.strip()
    return df
#change string date column to datetime
def date(df, col):
    df[col] = pd. to_datetime(df[col], errors= "coerce" ) 
    return df[col]
#remove full dublication after check primary key
def remove_duplication(df, col):
    df = df.drop_duplicates(subset= col,keep= "first")
    return df
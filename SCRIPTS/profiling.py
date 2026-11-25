# function to determine spaces in values
def profile_space_strings(df, cols):
    total_item_have_space = 0
    for col in cols:
        for item in df[col]:
            checkBeforeStrip = len(item)
            CheckAfterStrip = len(item.strip())
            if (checkBeforeStrip -CheckAfterStrip) > 0:
                total_item_have_space += 1
    if total_item_have_space > 0:
        return True
    else:
        return False   
# function to determine "" , nan   ," "  
def profile_empty(df, text_col):
   spaces_only = {}
   empty_string={}
   totalNan= df.isna().sum().to_dict()
   for col in text_col:
       empty_string[col]= int((df[col] == "").sum())
       spaces_only[col] =(df[col].str.strip() == "").sum() - empty_string[col]
   return totalNan, empty_string, spaces_only

def chk_empty_nan(df):
        total_nan =  df.isna().sum().to_dict()
        return total_nan
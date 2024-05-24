import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from functools import reduce

# print column-names
def print_column_names(dataframes):
    for df in dataframes:
    print(df.columns)
    print('-' * 30)

# change column-names to lower case and snake case
# 'dataframes' is a list of the dataframes
def columns_lower_snake_case(dataframes):
    for df in dataframes:
        df.columns = df.columns.str.lower()
        df.columns = df.columns.str.replace(' ', '_')

        print(df.columns)
        print('-' * 30)
    return dataframes
    
# delete unneeded columns
# 'dataframes' is a list of the dataframes
# 'dropping' is a list of the column_names to drop
def delete_columns(dataframes, dropping):
    for df in dataframes:
        df.drop(dropping, axis=1)   # axis=1 means columns_name

        print(df.columns)
        print('-' * 30)
    return dataframes

# drop the duplicates
def drop_duplicates(dataframes):
    for df in dataframes:
        df.drop_duplicates(inplace=True)
        print(df.duplicated().value_counts())
        print('---')
        #print(df.shape)
        #print('---')
        #print(df.columns)
        #print('-' * 30)
    return dataframes

# extract weekday from the date column
def extract_weekday(df):
    df['weekday'] = df['order_date'].dt.day_name()
    df.sample(10)
    return df

# convert the date columns to datetime format
# 'date_columns is a list of the date columns to convert to datetime format
def datetime_format(df, date_columns):
    for date_column in date_columns:
        df.['date_column'] = pd.to_datetime(df.['date_column'])
    df.info()
    return df


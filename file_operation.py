import pandas as pd
from data import data


# # Read data from python dict
# df = pd.DataFrame(data=data).T
# print(df)

# # Write data to csv file 
# df.to_csv('country_data.csv')


# # Read data from csv file
# df = pd.read_csv('country_data.csv',index_col=0)
# print(df)

# # Write data to xlsx file
# df.to_excel('country_data.xlsx')


# Read xl file

df = pd.read_excel('Spectora Scraping Projects.xlsx')
# print(df)
# print(df.loc['10006 Harr Knoll','Sqft'])
# print(df.dtypes)
print(df.dtypes['I. Structural Systems'])
df['I. Structural Systems'] = df['I. Structural Systems'].astype(str)
print(df.dtypes['I. Structural Systems'])
print(df.head(10))
for idx, row in df.iterrows():
    # print(idx)
    # print(row['Address'])
    # structural_system = row['I. Structural Systems']
    print(row)

    break
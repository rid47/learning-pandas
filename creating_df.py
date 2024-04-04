import numpy as np
import pandas as pd

d = {'x': [1, 2, 3], 'y': np.array([2, 4, 8]), 'z': 100}

df = pd.DataFrame(d)
# print(df)

df2 = pd.DataFrame(d,index=[10,20,30],columns=['z','y','x'])
# print(df2)


l = [{'x': 1, 'y': 2, 'z': 100},
     {'x': 2, 'y': 4, 'z': 100},
     {'x': 3, 'y': 8, 'z': 100}]

df_from_list = pd.DataFrame(l)
# print(f"{df_from_list=}")



l = [[1, 2, 100],
     [2, 4, 100],
     [3, 8, 100]]

df_from_nested_list = pd.DataFrame(l, columns=['x', 'y', 'z'])

# print(f"{df_from_nested_list=}")



df_from_csv = pd.read_csv('data.csv',index_col=0)

# print(f"{df_from_csv=}")

# print(df_from_csv.head)
# print(df_from_csv.index)
# print(df_from_csv.columns)
# print(df_from_csv.columns[0])
# print(df_from_csv.dtypes)
# print(df_from_csv.shape)
# print(df_from_csv.size)
# print(df_from_csv.memory_usage())
print(df_from_csv.memory_usage())
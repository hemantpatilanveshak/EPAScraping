import pandas as pd


col1 = []
col2 = []
col3 = []
col4 = []
# df_concat = pd.DataFrame({
#     "Col1" : col1,
#     "Col2" : col2,
#     "Col3" : col3,
#     "Col4" : col4,
# })

# df_concat = pd.concat(map(pd.read_csv , ['test.csv','soli_pollution.csv']),ignore_index=True,axis=0)

# df1 = pd.read_csv('test.csv')
# df2 = pd.read_csv('soli_pollution.csv')
# print(df1)
# print(df2)

# df_concat = pd.concat([df1.reset_index(drop=True),df2.reset_index(drop=True)],ignore_index=True,axis=0)
# print(df_concat)

# df_concat.to_csv("concat.csv",header=False,index=False)


csv_files = ['test.csv','soli_pollution.csv']

df_csv_append = pd.DataFrame()
df_list = []
for file in csv_files:
    # df = pd.read_csv(file,header=None)
    # df.to_csv("concat.csv",mode="a",header=False,index=False)
    # df_list.append(df)
    # df_csv_append = pd.concat(,ignore_index=True, axis=0)
    df = pd.read_csv(file,header=None)
    df_list.append(df)
    df = None

df_csv_append = pd.concat(df_list,ignore_index=True,axis=0)
# print(df_list)
# print(df_csv_append)
print(df_csv_append)
df_csv_append.to_csv("concat.csv",header=False,index=False)
import pandas as pd
import glob
import os


filepath = ".\csv_files\\"

file_list = os.listdir(filepath)
print(file_list)

for file in file_list:
    df = pd.read_csv(file)
    df.to_csv(".\csv_files\concat2.csv",mode="a",header=False,index=False)
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.epa.gov/air-quality-management-process/air-quality-management-process-cycle"
response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")

keywords = ['establishes goals','  emissions reductions',
            'scientific research',
            'developing control strategies','implement programs',' on-going evaluation']

col1 = []
col2 = []
col3 = []
col4 = []

a = soup.find_all(['p','li'])
for row in a:
    for key in keywords:
        if key in row.text:
            col1.append("Air Quality Management Process Cycle")
            col2.append(key)
            col3.append(row.text)
            col4.append(url)


# print(len(col1),len(col2))
# print(col1)

df = pd.DataFrame({
    "Topic" : col1,
    "Keywords" : col2 ,
    "Description" : col3,
    "Url" : col4,
})

# print(df)


df.to_csv("data.csv",mode='a',header=False,index=False)
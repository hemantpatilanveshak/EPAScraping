from bs4 import BeautifulSoup
import requests



url = "https://aqli.epic.uchicago.edu/pollution-facts/"



response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")
col1 = []
col2 = []
col3 = []
col4 = []

h1_tag = soup.find("h1")
print(h1_tag)


for tag in soup.find_all(["h2"]):
    if tag.text == "Discover.":
        break
    p_tag = tag.find_next_siblings()
    for p in p_tag:
        if p.name == "h2" or p.name == "h3":
            break
        print(tag.text.strip(),"-->",p.text.strip())
        col1.append(h1_tag.text)
        col2.append(tag.text.strip())
        col3.append(p.text.strip())
        col4.append(url)
        
for tag in soup.find_all(["h3"]):
    p_tag = tag.find_next_siblings()
    for p in p_tag:
        if p.name == "h2" or p.name == "h3":
            break
        print(tag.text.strip(),"-->",p.text.strip())
        col1.append(h1_tag.text)
        col2.append(tag.text.strip())
        col3.append(p.text.strip())
        col4.append(url)

print(len(col1),len(col2),len(col3))


print("Final Lenght-->",len(col1),len(col2),len(col3))

import pandas as pd

df = pd.DataFrame({
    "Col1" : col1,
    "Col2" : col2,
    "Col3" : col3,
    "Col4" : col4,
})

print(df)

df.to_csv("15_06.csv",mode="a",header=False,index=False)
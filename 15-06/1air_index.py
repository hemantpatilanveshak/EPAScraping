from bs4 import BeautifulSoup
import requests
import pandas as pd
url= "https://www.lung.org/clean-air/outdoors/air-quality-index"
response = requests.get("https://www.lung.org/clean-air/outdoors/air-quality-index")
soup = BeautifulSoup(response.content,"html.parser")

col1 = []
col2 = []
col3 = []
col4 = []

div = soup.find("div",class_="fr-view")
# print(div)

h2_tags = div.find("h2")
print(h2_tags)
h3_tags = div.find_all("h3")
print(h3_tags)
for tag in h3_tags:
    p_tag = tag.find_next_siblings()
    for i in p_tag:
        if i.name != "h3":
            print(tag.text,"-->",i.text)
            col1.append(h2_tags.text.strip())
            col2.append(tag.text.strip())
            col3.append(i.text.strip())
            col4.append(url)


print(len(col1),len(col2),len(col3),len(col4))

df = pd.DataFrame({
    "Col1" : col1,
    "Col2" : col2,
    "Col3" : col3,
    "Col4" : col4,
})

print(df)

df.to_csv("15_06.csv",header=False,index=False)
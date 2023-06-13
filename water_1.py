from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.fairplanet.org/story/types-and-effects-of-water-pollution/"
response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")

div_tag = soup.find("div",class_="article_details_text")
# print(div_tag)

h2_tag = div_tag.find_all(["h2","h3"])
print(h2_tag)

col1 = []
col2 = []
col3 = []
col4 = []

for i in h2_tag:
    str = ""
    print("#" + i.text.strip())
    col1.append("EFFECTS OF WATER POLLUTION?")
    col2.append(i.text.strip())
    col4.append(url)
    for s in i.find_next_siblings():
        if s.name == "p":
            print(s.text.strip())
            str = str + s.text.strip()
        else:
            col3.append(str)
            print("-----------")
            break

col3.append(str)
print("*********************")
# print(col3[16])  
# print(len(col2),len(col3))
        
df = pd.DataFrame({
    "col1" : col1,
    "col2" : col2,
    "col3" : col3,
    "col4" : col4,
})

print(df)

df.to_csv("effect_of_water_poulltion.csv",header=False,index=False)
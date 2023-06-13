from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://populationmatters.org/climate-change/"

response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")

h2_tag = soup.find_all("h2")
print(h2_tag)

# for tag in h2_tag:
#     print("#" + tag.text)
    
#     if tag.find_next_sibling().name == "p":
#         print(tag.find_next_sibling())
#     else:
#         print("-----------")
column1 = []
column2  =[]
column3 = []
str = ""

for e in soup.find_all('h2'):
    if e.text == "Related content":
        break
    else:
        column1.append("CLIMATE CHANGE")
        
        column2.append(e.text)
        print('# '+e.text)
        
    for s in e.find_next_siblings():
        if s.name == 'p':
            str = str + (s.get_text(strip=True))
            print(s.get_text(strip=True))
            
        else:
            column3.append(str)
            str = ""
            print('-----------------')
            break

topic = "CLIMATE CHANGE"
column4 = []
for i in range(len(column2)):
    column4.append(url)


# print(column1)
print(len(column1),len(column2),len(column3),len(column4))
# print(column2)
# print(column3)

df = pd.DataFrame({
    "Topic" : column1,
    "Keywords" : column2 ,
    "Description" : column3,
    "Url" : column4,
})

df.to_csv("data.csv",mode='a',header=False,index=False)
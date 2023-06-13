import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.epa.gov/acidrain/effects-acid-rain"

response = requests.get(url)
print(response)
soup = BeautifulSoup(response.content,"html.parser")
topic = "Effects of Acid Rain"

h2_tags = soup.find_all("h2")
h3_tags = soup.find_all("h3")
for row in h2_tags:
    row.name = 'h3'



# for row in soup.find_all("h3"):
#     for e in row.find_next_sibling():

column1 = []
column2 = []
column3 = []
column4 = []
a = []
str = ""



for e in soup.find_all('h3'):
    if e.text == "Discover.":
        break
    else:
        column1.append("Basic Ozone Layer Science")
        
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


for i in range(len(column1)):
    column4.append(url)

print(len(column1),len(column2),len(column3),len(column4))
print(column3)

df = pd.DataFrame({
    "Main Topic" : column1,
    "Sub Topic" : column2,
    "Description" : column3,
    "Url" : column4 ,

})

print(df)

df.to_csv("data.csv",mode='a',header=False,index=False)
import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://www.epa.gov/ozone-layer-protection/health-and-environmental-effects-ozone-layer-depletion"
url2 = "https://www.epa.gov/ozone-layer-protection/basic-ozone-layer-science"
response = requests.get(url2)
soup = BeautifulSoup(response.content,"html.parser")

column1 = []
column2 = []
column3 = []
column4 = []
a = []
str = ""


for e in soup.find_all('h2'):
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
column3.append(str)

for i in range(len(column1)):
    column4.append(url)
print(len(column1),len(column2),len(column3),len(column4))
# print(column3)


data = {
    "Column 1": column1,
    "Column 2": column2,
    "Column 3": column3,
    "Column 4": column4
}
df = pd.DataFrame(data)
df.to_csv("data.csv",mode='a',header=False, index=False)
print(df)
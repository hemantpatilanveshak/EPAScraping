from bs4 import BeautifulSoup
import requests
import pandas as pd


url1 = "https://www.epa.gov/acidrain/what-acid-rain"
response = requests.get(url1)

soup = BeautifulSoup(response.content,"html.parser")


col1 = []
col2 = []
col3 = []
col4 = []

topic = "Acid Rain"

h1 = soup.find('h1',class_='page-title')
print(h1.get_text())

col2.append(h1.get_text())

h1.find_all_next('p')

a =h1.find_all_next('p')
col3.append(a[0].get_text())

h2 = soup.find_all('h2')

for i in range(len(h2))[:3]:
    col2.append(h2[i])
    if h2[i].findAllNext('p'):
        col3.append(h2[i].findAllNext('p'))

for i in range(len(col2)):
    col1.append(topic)
    col4.append(url1)

print(len(col2),len(col3),len(col1),len(col4))

df = pd.DataFrame({
    "Main Topic" : col1,
    "Sub Topic" : col2,
    "Description" : col3,
    "Url" : col4 ,

})

df.to_csv("data.csv",index=False)

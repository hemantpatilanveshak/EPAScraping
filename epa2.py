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

h2 = soup.find("h2")
col1.append(h2.text.strip())

p_tag = soup.find_all("p")
print(len(p_tag))
for row in p_tag[5:]:
    print(row.text.strip())

# div_tag = h2.find_all_next('div')
# print(div_tag)

# print(col1,"---->" ,col2)


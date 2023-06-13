from bs4 import BeautifulSoup
import requests
import pandas as pd


url1 = "https://www.epa.gov/ozone-layer-protection/basic-ozone-layer-science"
response = requests.get(url1)

soup = BeautifulSoup(response.content,"html.parser")


col1 = []
col2 = []
col3 = []
col4 = []


tags = soup.find(["h2","p"])

for row in tags:
    if row.name == "h2":
        col2.append(row.text.strip())
        a = row.find_next().name
    




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

h1_tag = soup.find("h1")
if h1_tag:
    h1_content = h1_tag.text.strip()
    col1.append(topic)
    col2.append(h1_content)

    p_tag = h1_tag.find_next_sibling("p")
    if p_tag:
        p_content = p_tag.text.strip()
        col3.append(p_content)

h2_tags = soup.find_all("h2")
for h2_tag in h2_tags:
    h2_content = h2_tag.text.strip()
    col1.append(topic)
    col2.append(h2_content)
    
    p_tags = h2_tag.find_next_siblings("p")
    str = ""
    for p_tag in p_tags:
        p_content = p_tag.text.strip()
        str = str + p_content
        
    col3.append(str)
        
    # print("------------------")
    

print(col1)
print(col2)
print(col3)
# print(col2[6])
# print(len(col1),len(col2),len(col3))

    


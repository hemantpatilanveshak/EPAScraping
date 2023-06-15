from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.nrdc.org/stories/ocean-acidification-what-you-need-know"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
print(response)

col1 = []
col2 = []
col3 = []
col4 = []
# print(soup)

# [x.extract() for x in soup.findAll(['script','style'])]
# # print(soup)


article = soup.find("article")
h1_tag = soup.find("h1")
h2_tags = article.find_all("h2")
# print(h2)

for h2 in h2_tags:
    p_tag = h2.next_elements
    for p in p_tag:
        if p.name == "h2":
            break
        elif p.name == "p":
            print(h2.text,"-->",p.text.strip())
            col1.append(h1_tag.text.strip())
            col2.append(h2.text.strip())
            col3.append(p.text.strip())
            col4.append(url)


df = pd.DataFrame({
    "Col1" : col1,
    "Col2" : col2,
    "Col3" : col3,
    "Col4" : col4,
})

print(df)






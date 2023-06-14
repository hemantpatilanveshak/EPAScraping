from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get("https://www.hsph.harvard.edu/ehep/82-2/")

soup = BeautifulSoup(response.content,"html.parser")

article = soup.find("article")
# soup.next_elements
h4_tags = article.find_all("h4")

# print(h4_tags[0].next_elements)
# for i in h4_tags[0].next_elements:
#     print(i.name)

for tag in h4_tags:
    p_tag = tag.next_elements
    for p in p_tag:
        if p.name == "td":
            print(tag.text,"-->",p.text)
        elif p.name == "h4":
            break
        else:
            continue
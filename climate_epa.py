from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://www.epa.gov/climatechange-science/impacts-climate-change"

response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")

# h2_tags = soup.find_all("h2")
# print(h2_tags)
# str = ""
# for e in h2_tags[:]:
    
#     print("#",e.text)
#     for s in e.find_next_siblings():
#         if s.name != "h2":
#             str = str + s.text
#         else:
#             break
#         print(str)
#         print("---------------")  

div_tag = soup.find("div",class_="l-sidebar__main")

# print(div_tag)

h2_tag = div_tag.find_all("h2")
# print(h2_tag)
p_tag = div_tag.find_all("p")
# print(p_tag)

col1 = []
col2 = []
col3 = []
col4 = []
str = ""

for i in h2_tag:
    col1.append(i.text)
    for j in i.find_next_siblings():
        if j.name == 'p':
            str = str + j.text
        else:
            col2.append(str)
            break


print(len(col2))
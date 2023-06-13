import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.nrdc.org/stories/air-pollution-everything-you-need-know"

response = requests.get(url)
print(response)

soup = BeautifulSoup(response.content,"html.parser")

h2_tags = soup.find("h2")

for a in h2_tags.find_next_siblings():
    print(a.name)

col1 = []
col2 = []
col3  = []
col4 = []


# # for e in soup.find_all("h2"):
#     col1.append(e.text)
#     for s in e.find_next_siblings():
#         if s.name == 'p':
#             col2.append(s.text)
#         elif s.name == 'h3':
#             col1.append(s.text)
#             for q in s.find_next_siblings():
#                 if q.name == 'p':
#                     col2.append(q.text)
#                 elif q.name == 'h2':
#                     break
#         else:
#             print("-------------")
#             break


# print(len(col1),len(col2))

div_tags = soup.find_all('div',class_='c-wysiwyg')
div_tags.pop()

print(len(div_tags))
for a in div_tags[::2]:     
    # print(a.text.strip())
    col1.append(a.text.strip())

for a in div_tags[1::2]:
    # print(a.text.strip())
    col2.append(a.text.strip())
    col3.append(url)

print(len(col1),len(col2))
col4 = []
topic = "Air Pollution"
for i in range(len(col1)):
    col4.append(topic)


df = pd.DataFrame({
    "Main Topic" : col4,
    "Sub Topic" : col1,
    "Description" : col2,
    "Url" : col3 ,

})

df.to_csv("data.csv",mode='a',header=False,index=False)

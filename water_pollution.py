import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iberdrola.com/sustainability/water-pollution"

response = requests.get(url)
print(response)

soup = BeautifulSoup(response.content,"html.parser")

# h2_tags = soup.find_all(["h2","h3"])
# for i in h2_tags[4:-4]:
#     print("#" + i.text.strip())
#     for s in i.find("p"):
#         if s.name != "h2" or "h3":
#             print(s.text.strip())
#         else:
#             break
# soup.find_next()
# p_tags = soup.find_all()
# df.to_csv("test.csv",mode='a',header=False,index=False)

h3_tags = soup.find_all("h3")




h4_tags = soup.find_all("h4")
# print(head[0])
# print(head[0].find_next_sibling())
# for i in head:
#     print(i.text)

col1  =[]
col2 = []
col3 = []
col4 = []
# str = ""

# for i in head:
#     str = ""
#     # print("#" + i.text)
#     col1.append("WATER POLLUTION")
#     col2.append(i.text.strip())
#     for j in i.find_next_siblings():
#         if j.name != 'h3':
#             # print(j.text.strip())
#             str = str + j.text.strip()
#         else:
#             col3.append(str)
#             break
# print("-------------")
# # print(str)
# print(len(col1),len(col2),len(col3),len(col4))
# # print(col3[0])


for i in h3_tags:
    str = ""
    col1.append("WATER POLLUTION")
    print(i.text)
    col2.append(i.text)
    col4.append(url)
    for s in i.find_next_siblings():
        if s.name == 'p':
            print(s.text.strip())
            str = str + s.text.strip()
        else:
            col3.append(str)
            print("-----------")
            break

print("*****************")
p = soup.find_all("p")
print(p)
print("*****************")
print(len(col1),len(col2),len(col3),len(col4))

print(col3)

# df = pd.DataFrame({
#     "col1":col1,
#     "col2" : col2,
#     "col3" : col3,
#     "col4" : col4,
# })
    
# print(df)

# df.to_csv("water_pollution.csv",mode = 'a',header=False,index=False)

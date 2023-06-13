# url = "https://www.envirotech-online.com/news/water-wastewater/9/breaking-news/6-effects-of-water-pollution/57707"

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# response = requests.get(url)
# print(response)

# soup = BeautifulSoup(response.content,"html.parser")


# col1  =[]
# col2 = []
# col3 = []
# col4 = []
# str = ""



# h2_tags = soup.find_all("h2")
# for i in h2_tags:
#     str = ""
#     col1.append("Land and soil pollution")
#     print(i.text)
#     col2.append(i.text)
#     col4.append(url)
#     for s in i.find_next_siblings():
#         if s.name == 'p':
#             print(s.text.strip())
#             str = str + s.text.strip()
#         else:
#             col3.append(str)
#             print("-----------")
#             break

# # print(col3[6])
# print(len(col1),len(col2),len(col3),len(col4))

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://earth.org/what-are-the-causes-of-water-pollution/"
response = requests.get(url)
print(response)

soup = BeautifulSoup(response.content,"html.parser")

for i in soup.find_all("h3"):
    print(i.text)
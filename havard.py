from bs4 import BeautifulSoup
import requests
import pandas as pd


urls = ["https://www.hsph.harvard.edu/ehep/air-pollution/",
        "https://www.hsph.harvard.edu/ehep/biological-pollution/",
        "https://www.hsph.harvard.edu/ehep/noise-pollution/",
        "https://www.hsph.harvard.edu/ehep/82-2/",
        ]

col1 = []
col2 = []
col3 = []
col4 = []

# for url in urls:
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content,"html.parser")
#     article = soup.find("article")
#     next_tags = article.next_elements
#     h1_tag = article.find("h1")
#     for i in next_tags:
#         if i.name == "h4":
#             #check i.next_elements
#             temp = i.next_elements
#             for j in temp:
#                 if j.name == "p":
#                     print(f"{i.text.strip()}-->{j.text.strip()}")
#                     col1.append(h1_tag.text.strip())
#                     col2.append(i.text.strip())
#                     col3.append(j.text.strip())
#                     col4.append(url)
#                 elif j.name == "h4":
#                     break

#     h4_tags = article.find_all("h4")

#     for tag in h4_tags:
#         p_tag = tag.next_elements
#         for p in p_tag:
#             if p.name == "td":
#                 print(tag.text,"-->",p.text)
#                 col1.append(h1_tag.text.strip())
#                 col2.append(tag.text.strip())
#                 col3.append(p.text.strip())
#                 col4.append(url)
                
#             elif p.name == "h4":
#                 break
#             else:
#                 continue

#     for tag in h4_tags:
#         next_h4_tag = tag.find_next_sibling("h4")
#         print

#     # for i in next_tags:
#     #     if i.name == "h3":
#     #         temp = i.next_elements
#     #         for j in temp


response = requests.get(urls[2])
soup = BeautifulSoup(response.content,"html.parser")
article = soup.find("article")
h4_tags = article.find_all("h4")
for tag in h4_tags:
    next_h4_tag = tag.find_next_sibling()
    print(next_h4_tag.name)
# print(len(col1),len(col2),len(col3),len(col4))


# df = pd.DataFrame({
#     "Col1" : col1,   
#     "Col2" : col2,
#     "Col3" : col3,
#     "Col4" : col4,
# })

# print(df)

# df.to_csv("air_pollution_harvard.csv",header=False,index=False)





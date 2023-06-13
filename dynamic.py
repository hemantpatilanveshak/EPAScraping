from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.epa.gov/so2-pollution/sulfur-dioxide-basics"
url2 = "https://www.epa.gov/so2-pollution/setting-and-reviewing-standards-control-so2-pollution"
url3 = "https://www.epa.gov/so2-pollution/applying-or-implementing-sulfur-dioxide-standards"
url4 = "https://www.epa.gov/so2-pollution/primary-national-ambient-air-quality-standard-naaqs-sulfur-dioxide"
url5 = "https://www.epa.gov/so2-pollution/applying-or-implementing-sulfur-dioxide-standards"
url6 = "https://www.epa.gov/acidrain/what-acid-rain"
url7 = "https://www.airnow.gov/aqi/aqi-basics/"
url8 = "https://www.epa.gov/lead/learn-about-lead"
url9 = "https://www.epa.gov/lead/protect-your-family-sources-lead"
url10 = "https://www.epa.gov/lead/lead-laws-and-regulations"
response = requests.get(url10)
soup = BeautifulSoup(response.content,"html.parser")

# h1_tags = soup.find("h1",class_="page-title")
# print(h1_tags.text.strip())

# try:
#     article = soup.find("article",class_="article")
    
#     for e in article.find_all("h2"):
#         print("h2->",e.text)
#         for s in e.find_next_siblings():
#             if s.name == "p":
#                 print("p->",s.text)
#             if s.name == "h3":
#                 # j = s.find_next_siblings()
#                 print("h3->",s.text)
#                 for tag in s.find_next_siblings():
#                     if tag.name == "p":
#                         print(tag.text)
#                     else:
#                         break
#             if s.name == "div":
#                 print("Div-->",s.text)
# except:
#     print("-")

# try:
#     article = soup.find("article",class_="article")
    
#     for e in article.find_all("h2"):
#         for s in e.find_next_siblings():
#             if s.name == "div":
#                 print("Div-->",s.text)
#             else:
#                 for j in s.find_next_siblings():
#                     if j.name == "p":
#                         print("Div p -->",j.text)
# except:
#     print("-")

# try:
#     article = soup.find("article",class_="article")
#     for e in article.find_all("h2"):
#         j = e.find_next_sibling()
#         if j.name == "h3":
#             for p_tags in j.find_next_siblings():
#                 print(f"{j.name}-->{j.text}")
#                 if p_tags.name == "p":
#                     print(f"{p_tags.name}--> {p_tags.text}")
#                 elif p_tags.name == "div":
#                     print(f"{p_tags.name} --> {p_tags.text}")
#                 elif p_tags.name == "h3":
#                     for p_tags_h3 in p_tags.find_next_siblings():
#                         print(f"{p_tags_h3.name}--> {p_tags_h3.text}")
#                         if p_tags_h3.name == "p":
#                             print(f"{p_tags_h3.name}--> {p_tags_h3.text}")
#                         elif p_tags_h3.name == "div":
#                             print(f"{p_tags_h3.name} --> {p_tags_h3.text}")
#                         elif p_tags_h3.name == "h2":
#                             break

#                 elif p_tags.name == "h2":
#                     break

#         # j = p_tags
     



# except:
#      print("-") 



# try:
#     #h2 tags
#     h2_tags = soup.find_all("h2")
#     for h2 in h2_tags:
#         p_tag = h2.find_next_sibling('p')
#         if p_tag:
#             print(h2.text,"-->",p_tag.text)
# except:
#     print("-")


# try:
#     h2_tag = soup.find("h2")

#     h2_next = h2_tag.next_elements

#     for i in h2_next:
#         if i.name == "p":
#             print(i.text)
#         if i.name =="h2" or i.name == "h3":
#             continue


# except:
#     pass

# article = soup.find("article",class_="article")


# h2_tag = article.find("h2") 
# for i in range(30):
    
#     if h2_tag.find_next_sibling().name == "p":
#         print(h2_tag.text,"-->" ,h2_tag.find_next_sibling().text)
#     elif h2_tag.find_next_sibling().name == "div":
#         print(h2_tag.text,"-->", h2_tag.find_next_sibling().text)
#     elif h2_tag.find_next_sibling().name == "h3":
#         pass

#     try:
#         h2_tag = h2_tag.find_next_sibling()
#         if h2_tag.text == None:
#             break

#     except:
#         break
# d = {}
# for p in soup.select('p'):
#     if p.find_previous('h2'):
#         if d.get(p.find_previous('h2').text) == None:
#             d[p.find_previous('h2').text]=[]
#     else:
#         continue
#     d[p.find_previous('h2').text].append(p.text)

# # print(d)


# for p in soup.select('p'):
#     if p.find_previous('h3'):
#         if d.get(p.find_previous('h3').text) == None:
#             d[p.find_previous('h3').text]=[]
#     else:
#         continue
#     d[p.find_previous('h3').text].append(p.text)

# print(d)

data = []

for p in soup.find_all(["h2","h3"]):
    if p.text == "Discover.":
        break
    # print(p.text)
    p_tag = p.next_elements
    for i in p_tag:
        if i.name == "p" or i.name == "li":
            # print(i.text.strip())
            data.append({"h2 or h3":p.text.strip().replace("\xa0"," "),"p":i.text.strip().replace("\xa0"," ")})
        elif i.name == "h2" or i.name == "h3":
            break

print(data)  
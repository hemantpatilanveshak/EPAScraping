

from bs4 import BeautifulSoup
import requests


url = "https://www.niehs.nih.gov/health/topics/agents/air-pollution/index.cfm"

urls = [url]





# response = requests.get(url11)

# soup = BeautifulSoup(response.content,"html.parser")
col1 = []
col2 = []
col3 = []
col4 = []


try:
    for i in range(len(urls)):
        site = requests.get(urls[i])
        soup = BeautifulSoup(site.content,"html.parser")
        h1_tag = soup.find("h1")

        soup1 = soup.find("article")
        for tag in soup1.find_all(["h2"]):
            if tag.text == "Discover.":
                break
            p_tag = tag.find_next_siblings()
            for p in p_tag:
                if p.name == "h2" or p.name == "h3" or p.name == "h4":
                    break
                print(tag.text.strip(),"-->",p.text.strip())
                col1.append(h1_tag.text.strip())
                col2.append(tag.text.strip())
                col3.append(p.text.strip())
                col4.append(urls[i])
                
        for tag in soup1.find_all(["h3"]):
            p_tag = tag.find_next_siblings()
            for p in p_tag:
                if p.name == "h2" or p.name == "h3" or p.name == "h4":
                    break
                print(tag.text.strip(),"-->",p.text.strip())
                col1.append(h1_tag.text.strip())
                col2.append(tag.text.strip())
                col3.append(p.text.strip())
                col4.append(urls[i])

        for tag in soup1.find_all(["h4"]):
            p_tag = tag.find_next_siblings()
            for p in p_tag:
                if p.name == "h2" or p.name == "h3" or p.name == "h4":
                    break
                print(tag.text.strip(),"-->",p.text.strip())
                col1.append(h1_tag.text.strip())
                col2.append(tag.text.strip())
                col3.append(p.text.strip())
                col4.append(urls[i])

        print(len(col1),len(col2),len(col3))
except:
    col1.append("-")
    col2.append("-")
    col3.append("-")

print("Final Lenght-->",len(col1),len(col2),len(col3),len(col4))

import pandas as pd

df = pd.DataFrame({
    "Col1" : col1,
    "Col2" : col2,
    "Col3" : col3,
    "Col4" : col4
})

print(df)
# csv_file = df.to_csv("multiple_url_data_text.csv",header=False,index=False)


df.to_csv("15_06.csv",mode="a",header=False,index=False)
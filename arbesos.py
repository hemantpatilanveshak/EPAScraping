url = "https://www.epa.gov/asbestos/learn-about-asbestos#asbestos"
url2 = "https://www.britannica.com/science/water-pollution"

from bs4 import BeautifulSoup
import requests



urls = [ url]





# response = requests.get(url11)

# soup = BeautifulSoup(response.content,"html.parser")
col1 = []
col2 = []
col3 = []
col4 = []

for i in range(len(urls)):
    site = requests.get(urls[i])
    soup = BeautifulSoup(site.content,"html.parser")

    for tag in soup.find_all(["h2"]):
        if tag.text == "Discover.":
            break
        p_tag = tag.find_next_siblings()
        for p in p_tag:
            if p.name == "h2" or p.name == "h3":
                break
            print(tag.text.strip(),"-->",p.text.strip())
            col1.append(tag.text.strip())
            col2.append(p.text.strip())
            col3.append(urls[i])
            
    for tag in soup.find_all(["h3"]):
        p_tag = tag.find_next_siblings()
        for p in p_tag:
            if p.name == "h2" or p.name == "h3":
                break
            print(tag.text.strip(),"-->",p.text.strip())
            col1.append(tag.text.strip())
            col2.append(p.text.strip())
            col3.append(urls[i])

    print(len(col1),len(col2),len(col3))


print("Final Lenght-->",len(col1),len(col2),len(col3))

import pandas as pd

df = pd.DataFrame({
    "Col1" : col1,
    "Col2" : col2,
    "Col3" : col3,
})

print(df)
# csv_file = df.to_csv("multiple_url_data.csv",header=False,index=False)

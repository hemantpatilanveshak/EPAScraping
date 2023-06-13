from bs4 import BeautifulSoup
import requests



urls = [ "https://www.epa.gov/p2/learn-about-pollution-prevention",
 "https://www.epa.gov/p2/pollution-prevention-law-and-policies",
 "https://www.energy.gov/eere/why-clean-energy-matters",
 "https://www.epa.gov/climatechange-science/basics-climate-change",
 "https://www.epa.gov/watersense/watersense-labeled-homes",
 "https://www.epa.gov/watersense/about-watersense",
 "https://www.greenpeace.org/usa/oceans/preventing-plastic-pollution/",
 "https://kids.nationalgeographic.com/science/article/pollution",
 "https://www.nrdc.org/stories/air-pollution-everything-you-need-know#whatis",
 "https://www.who.int/news-room/fact-sheets/detail/ambient-(outdoor)-air-quality-and-health",
 "https://www.agrivi.com/blog/environmental-pollution/",]





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

csv_file = df.to_csv("multiple_url_data.csv",header=False,index=False)

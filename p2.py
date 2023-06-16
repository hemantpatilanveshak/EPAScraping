from bs4 import BeautifulSoup
import requests

url = "https://www.epa.gov/p2/learn-about-pollution-prevention"
url2 = "https://www.epa.gov/p2/pollution-prevention-law-and-policies"
url3 = "https://www.energy.gov/eere/why-clean-energy-matters"
url4 = "https://www.epa.gov/climatechange-science/basics-climate-change"
url5 = "https://www.epa.gov/watersense/watersense-labeled-homes"
url6 = "https://www.epa.gov/watersense/about-watersense"
url7 = "https://www.greenpeace.org/usa/oceans/preventing-plastic-pollution/"
url8 = "https://kids.nationalgeographic.com/science/article/pollution"
url9 = "https://www.nrdc.org/stories/air-pollution-everything-you-need-know#whatis"
url10 = "https://www.who.int/news-room/fact-sheets/detail/ambient-(outdoor)-air-quality-and-health"
url11 = "https://www.agrivi.com/blog/environmental-pollution/"
url12  = "https://www.epa.gov/p2/learn-about-pollution-prevention"
response = requests.get(url9)

soup = BeautifulSoup(response.content,"html.parser")
col1 = []
col2 = []
col3 = []
col4 = []
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
        
        
for tag in soup.find_all(["h3"]):
    p_tag = tag.find_next_siblings()
    for p in p_tag:
        if p.name == "h2" or p.name == "h3":
            break
        print(tag.text.strip(),"-->",p.text.strip())
        col1.append(tag.text.strip())
        col2.append(p.text.strip())
        # col3.append(url11)

print(len(col1),len(col2))


import pandas as pd

df = pd.DataFrame({
    "Col1" : col1,
    "Col2" : col2,
})





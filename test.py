from bs4 import BeautifulSoup
import requests


url = "https://www.epa.gov/so2-pollution/sulfur-dioxide-basics"
url2 = "https://www.epa.gov/so2-pollution/setting-and-reviewing-standards-control-so2-pollution"
response = requests.get(url2)
soup = BeautifulSoup(response.content,"html.parser")

data = []



h2_tags = soup.find_all('h2')
for h2 in h2_tags:
    
    p_tag = h2.find_next_siblings('p',limit = 2)
    
    if p_tag:
        data.append({'h2': h2.text, 'p': [p.text for p in p_tag]})

h3_tags = soup.find_all('h3')
for h3 in h3_tags:
    
    p_tags = h3.find_next_siblings('p', limit=3)
    if p_tags:
        data.append({'h3': h3.text, 'p': [p.text for p in p_tags]})


for item in data:
    print(item)

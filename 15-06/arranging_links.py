from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
base_url = "https://www.epa.gov"
url = "https://www.epa.gov/environmental-topics/air-topics"
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")

url1 = response.url
print(url1)
# all_links = soup.find_all("a",)

# print(all_links)
# for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
#     # display the actual urls
#     print(link.get('href'))  

main_tag = soup.find("main")

for link in main_tag.find_all('a'):
    if link.get('href').startswith('https://'):
        print("**",link.get('href'))
    else:
        
        print(base_url+link.get('href'))


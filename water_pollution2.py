import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.ducksters.com/science/environment/water_pollution.php"

response = requests.get(url)
print(response)

soup = BeautifulSoup(response.content,"html.parser")

b_tag = soup.find_all("b")
for i in b_tag[:-4]:
    print("#" + i.text.strip())
    for s in i.find_next_siblings():
        if s.name != 'b':
            print(s.text.strip())
        else:
            print("---------------")
            break



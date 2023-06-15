from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get("https://www.biologydiscussion.com/ecology/eutrophication-meaning-types-and-effects-ecology/57751")
soup = BeautifulSoup(response.content,"html.parser")

print(response)
# h1 = soup.find_all("h1")
# print(h1)
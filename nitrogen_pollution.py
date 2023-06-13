from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.conserve-energy-future.com/impact-solutions-nitrogen-pollution.php"
response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")
print(response)

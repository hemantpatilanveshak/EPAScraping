from bs4 import BeautifulSoup
import requests

url = "https://www.nrdc.org/stories/air-pollution-everything-you-need-know#causes"

response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")

div_class = soup.find_all("div",class_="c-wysiwyg")

for tag in div_class:
    h2_tag = tag.find()
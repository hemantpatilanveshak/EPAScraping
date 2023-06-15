from bs4 import BeautifulSoup
import requests
import json

url = "https://www.iberdrola.com/sustainability/water-pollution"
response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")

col1 = []
col2 = []
col3 = []
col4 = []


h2_tag = soup.find_all("h2")
print(h2_tag)

for h2 in h2_tag:
    p_tag = h2.next_elements
    for p in p_tag:
        if p.name == "h2" or p.name == "h3" or p.name == "h4":
            break
        elif p.name == "p":
            print(f"{h2.text.strip()}-->{p.text.strip()}")

h3_tag = soup.find_all("h3")
for h3 in h3_tag:
    p_tag = h3.next_elements
    for p in p_tag:
        if p.name== "h2" or p.name == "h3" or p.name == "h4":
            break
        elif p.name == "p":
            print(f"{h3.text.strip()}-->{p.text.strip()}")
        elif p.name == "ul":
            li = p.next_elements
            for j in li:
                if j.name == "h2" or j.name == "h3" or j.name == "h4" or j.name == "p":
                    break
                elif j.name == "li":
                    if j.strong:
                        print("*************Heloo********************")
                    else:
                        # print("**********************Not found*********************")
                        print(f"{p.text.strip()}-->{j.text.strip()}")

h4_tag = soup.find_all("h4")
for h4 in h4_tag:
    p_tag = h4.next_elements
    for p in p_tag:
        if p.name == "h2" or p.name == "h3" or p.name == "h4":
            break
        elif p.name == "p":
            print(f"{h4.text.strip()}-->{p.text.strip()}")
        elif p.name == "ul":
            li = p.next_elements
            for j in li:
                if j.name == "h2" or j.name == "h3" or j.name == "h4" or j.name == "p":
                    break
                elif j.name == "li":
                    print(f"{j.strong.text.strip()}-->{j.text.strip()}")


    

        
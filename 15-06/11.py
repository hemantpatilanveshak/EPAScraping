



from bs4 import BeautifulSoup
import requests


# url = "https://www.nrdc.org/stories/ocean-acidification-what-you-need-know"
url = "https://www.niehs.nih.gov/health/topics/agents/indoor-air/index.cfm"
# url = "https://www.epa.gov/acidrain/what-acid-rain"
# url = "https://www.epa.gov/greenvehicles/learn-about-green-vehicles"
# url ="https://populationmatters.org/climate-change/"
# url = "https://www.nrdc.org/stories/ocean-pollution-dirty-facts"
# url = "https://world-nuclear.org/information-library/nuclear-fuel-cycle/nuclear-wastes/radioactive-waste-management.aspx"
# url = "https://www.nrc.gov/reading-rm/doc-collections/fact-sheets/radwaste.html"
url = "https://www.lung.org/clean-air/outdoors/air-quality-index"

urls = [url]





# response = requests.get(url11)

# soup = BeautifulSoup(response.content,"html.parser")


col1 = []
col2 = []
col3 = []
col4 = []


try:
    for i in range(len(urls)):
        site = requests.get(urls[i])
        soup = BeautifulSoup(site.content,"html.parser")
        # soup2 = soup.find("div", class_="ArticleContent")
        # print("********",soup2)
        if soup.find("article") is not None:
            soup1 = soup.find("article")
            h1_tag = soup.find("h1")
        elif soup.find("div", class_="ArticleContent") is not None:
            soup1 = soup.find("div", class_="ArticleContent")
            h1_tag = soup1.find("h1")
        elif soup.find("div",id="post") is not None:
            soup1 = soup.find("div",id="post")
            h1_tag = soup1.find("h1")
        else:
            soup1 = soup
            h1_tag = soup1.find("h1")
        
        # print("*****",soup1)
        

        for tag in soup1.find_all(["h2"]):
            if tag.text == "Discover.":
                break
            p_tag = tag.find_next_siblings()
            for p in p_tag:
                if p.name == "h2" or p.name == "h3" or p.name == "h4":
                    break
                print(tag.text.strip(),"-->",p.text.strip())
                col1.append(h1_tag.text.strip())
                col2.append(tag.text.strip())
                col3.append(p.text.strip())
                
                
        for tag in soup1.find_all(["h3"]):
            p_tag = tag.find_next_siblings()
            for p in p_tag:
                if p.name == "h2" or p.name == "h3" or p.name == "h4":
                    break
                print(tag.text.strip(),"-->",p.text.strip())
                col1.append(h1_tag.text.strip())
                col2.append(tag.text.strip())
                col3.append(p.text.strip())
                

        for tag in soup1.find_all(["h4"]):
            p_tag = tag.find_next_siblings()
            for p in p_tag:
                if p.name == "h2" or p.name == "h3" or p.name == "h4":
                    break
                print(tag.text.strip(),"-->",p.text.strip())
                col1.append(h1_tag.text.strip())
                col2.append(tag.text.strip())
                col3.append(p.text.strip())
                

        print(len(col1),len(col2),len(col3))
except:
    col1.append("-")
    col2.append("-")
    col3.append("-")
    col4.append("-")

print("Final Lenght-->",len(col1),len(col2),len(col3),len(col4))

import pandas as pd

df = pd.DataFrame({
    "title" : col1,
    "subtitle" : col2,
    "description" : col3,
})

print(df)
# csv_file = df.to_csv("multiple_url_data_text.csv",header=False,index=False)
# df.to_csv("15_06.csv",mode="a",header=False,index=False)
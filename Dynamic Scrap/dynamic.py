from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrapper(url,file_name):
    try:
        col1 = []
        col2 = []
        col3 = []
        try:        
            site = requests.get(url)
        except:
            print("Site Not Found")
            
            
        soup = BeautifulSoup(site.content,"html.parser")
        
        if soup.find("article") is not None:
            test = soup.find_all("article")
            # soup1 = soup.find("article")
            soup1 = test[0]
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
                elif tag.text.strip() == "Select Your Location":
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
                elif tag.text.strip() == "Select Your Location":
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
                elif tag.text.strip() == "Select Your Location":
                    break
                print(tag.text.strip(),"-->",p.text.strip())
                col1.append(h1_tag.text.strip())
                col2.append(tag.text.strip())
                col3.append(p.text.strip())

        
        if test[1].find("h2") is None:
            p_tags = soup1.find_all("p")
            for p in p_tags:
                col1.append(h1_tag.text.strip())
                col2.append("-")
                col3.append(p.text.strip())



                    

        # print(len(col1),len(col2),len(col3))
    except:
        col1.append("-")
        col2.append("-")
        col3.append("-")

    try:
        df = pd.DataFrame({
             "title" : col1,
             "sub_title" : col2,
            "description" : col3,
                })
    except:
        print("Error in data frame")

    name = f"{file_name}.csv"
    df.to_csv(name)

    return name


url = input("Enter Url: ")
file_name = input("Enter a file name to save file: ")
output = scrapper(url,file_name)
print(output)
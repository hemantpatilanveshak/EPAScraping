from bs4 import BeautifulSoup
import requests
import pandas as pd



# url = "https://aqli.epic.uchicago.edu/pollution-facts/"
# url2 = "https://www.epa.gov/indoor-air-quality-iaq/introduction-indoor-air-quality#:~:text=Indoor%20Air%20Quality%20(IAQ)%20refers,risk%20of%20indoor%20health%20concerns."


def scrapper(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content,"html.parser")
    col1 = []
    col2 = []
    col3 = []
    col4 = []

    h1_tag = soup.find("h1")
    print(h1_tag)


    for tag in soup.find_all(["h2"]):
        if tag.text == "Discover.":
            break
        p_tag = tag.find_next_siblings()
        for p in p_tag:
            if p.name == "h2" or p.name == "h3":
                break
            print(tag.text.strip(),"-->",p.text.strip())
            col1.append(h1_tag.text)
            col2.append(tag.text.strip())
            col3.append(p.text.strip())
            col4.append(url)
            
    for tag in soup.find_all(["h3"]):
        p_tag = tag.find_next_siblings()
        for p in p_tag:
            if p.name == "h2" or p.name == "h3":
                break
            print(tag.text.strip(),"-->",p.text.strip())
            col1.append(h1_tag.text.strip())
            col2.append(tag.text.strip())
            col3.append(p.text.strip())
            col4.append(url)

    # print(len(col1),len(col2),len(col3))


    print("Final Lenght-->",len(col1),len(col2),len(col3))


    df = pd.DataFrame({
        " " : col1,
        "Col2" : col2,
        "Col3" : col3,
        "Col4" : col4,
    })
    print(df.columns)
    file_name = "indoor_air_quality_4.csv"
    df.to_csv(file_name)

    return file_name


url = input("Enter link to scrap: ")
file_name = scrapper(url)
print(file_name)
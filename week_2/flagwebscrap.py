import requests
from bs4 import BeautifulSoup

def titlefinder(str):
    title = []
    for i in str[0]:
        title.append(i)
        if (i=='<'):
            break
    return title[0]

    
def pic_download(title,link):
    response = requests.get("https:"+link)
    file = open(title + '.png', "wb")
    file.write(response.content)
    file.close()

def scrap_followers():
    base_url = "https://www.countryflags.com/"
    res = requests.get(base_url)
    soup = BeautifulSoup(res.content,"html.parser")
    followers = soup.select("div.thumb")
    str_title = []
    str_link = []
    for i in followers:
        str_title.append(i.select("span[class]"))
    for link in soup.find_all('img'):
        str_link.append(link.get('src'))
    index=0
    while(True):
        print(f"{index}/220 Files Downloaded\n")
        try:
           pic_download(titlefinder(str_title[index]),str_link[index+5])
        except:
            break
        index += 1
    print("\n\nALL PICS DOWNLOADED!")
   

def main():
    print("URL: www.countryflags.com\nDownloading.... \n")
    scrap_followers()
if __name__ == "__main__" :
    main()  
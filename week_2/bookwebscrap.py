import requests
from bs4 import BeautifulSoup
import urllib.request 

def titlefinder(str):
    title = []
    for i in str[0]:
        title.append(i)
        if (i=='<'):
            break
    return title[0]

    
def pic_download(title,link):
    urllib.request.urlretrieve(link,title + '.png')

def scrap_followers(index):
    base_url = "https://www.countryflags.com/"
    res = requests.get(base_url)
    print(res.status_code)
    soup = BeautifulSoup(res.content,"html.parser")
    followers = soup.select("div.thumb")
    str_title = []
    str_link = []
    for i in followers:
        str_title.append(i.select("span[class]"))
    
    for link in soup.find_all('img'):
        str_link.append(link.get('src'))
    pic_download(titlefinder(str_title[index]),str_link[index])
   

    #for i in range(len(str_title)):
    #    title = titlefinder(str_title[i])
    #   print(title)

def main():
    scrap_followers(0)


if __name__ == "__main__" :
    main()  
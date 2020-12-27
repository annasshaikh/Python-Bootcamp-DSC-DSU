# DSC-DSU | Python Bootcamp 2020 | Assigments Week 2

Assignments For DSC-DSU Python Boot Camp 

## Assigment 2

Scrapped the Facebook to Get Its Page Like.

## Assignment 4
#### Questains: Build a school scraper that'll scrap 50 schools' info and generate a CSV.

- Locate the API endpoint of the following education directory

  [https://directory.ntschools.net/#/schools](https://directory.ntschools.net/#/schools)

- Using BS4 only for the main page and JSON + Requests libraries for interacting with those endpoints
- Produce a well structured CSV with the following fields:
  1. School name
  2. Single lined formatted physical address
  3. Principal/Admin Name
  4. Principal/Admin Position
  5. Principal/Admin Email
  6. School Telephone number


#### Well Here Is My Approch: 
```python
#All The Libary Request
import requests 
import json
from csv import DictWriter

link = "https://directory.ntschools.net/api/System/GetAllSchools"   #BaseUrl saved In Link
res = requests.get(link)                                            #Geting Content From res
formated_res = json.loads(res.content)                              #Formating JSON data

link = 'https://directory.ntschools.net/api/System/GetSchool?itSchoolCode='
                                                                    #API Url For This Website
with open("school_data.csv","w",encoding="utf-8") as file:                 #Creating The data.csv With Headers
    file.write(",Name,Address,Principal/Admin Name,Position,Email,TelePhone\n")

school_codes = []                                                   #Storing All The School Code in a list
for i in formated_res:                                              #To append in the API Url
    school_codes.append(i['itSchoolCode'])

for i in range(50):                                                 #For 50 School
    school_data = requests.get(link+school_codes[i])
    data = json.loads(school_data.content)
    
    print(f"School #{i+1}")                                         #Prining Data For Each School
    print(data['name'])
    print(data['physicalAddress']['displayAddress'])
    print(data['schoolManagement'][0]['firstName']+ " " + data['schoolManagement'][0]['lastName'])
    print(data['schoolManagement'][0]['position'])
    print(data['schoolManagement'][0]['email'])
    print(data['telephoneNumber'])
    print("-------------------------")

    with open("school_data.csv","a",encoding="utf-8") as file:             #Storing The data In a data.csv File
        file.write(f",{data['name']},{data['physicalAddress']['displayAddress'].replace(',',' ')},{data['schoolManagement'][0]['firstName'] + ' ' + data['schoolManagement'][0]['lastName']},{data['schoolManagement'][0]['position']},{data['schoolManagement'][0]['email']},{data['telephoneNumber']}\n")

```
#### Csv Output: 
<a href="https://ibb.co/YLHrsBM"><img src="https://i.ibb.co/d58hY4q/school-data-Output.png" alt="school-data-Output" border="0"></a>


## Flag Downloader
I Tried to scrap a [website that contain all countrys flag](https://www.countryflags.com/) and download all posible flags on that website.
And well I came up with this code:
##### Note: Use delete_flag.py to clear all flags. MAKE SURE THERE NO OTHER PICTURES IN THAT DIRECTORY
```python
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
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


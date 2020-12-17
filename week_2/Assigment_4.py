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


